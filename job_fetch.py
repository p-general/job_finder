import requests

class Job_Finder:
    def __init__(self):
        self.app_id = "REDACTED_APP_ID"
        self.app_key = "REDACTED_APP_KEY"

    def job_fetcher(
        self,
        country_code="us",
        limit=100,
        sort_by="date",
        full_time=0,
        part_time=0,
        contract=0,
        permanent=0,
        location=None
    ):
        """
        Fetch jobs from Adzuna API.

        Args:
            country_code (str): 2-letter country code ('us', 'gb', etc.)
            limit (int): number of results
            sort_by (str): 'date', 'salary', 'relevance'
            full_time, part_time, contract, permanent (int): 0 or 1
            location (str, optional): city or area
        Returns:
            List of dicts containing job info
        """

        base_url = f"https://api.adzuna.com/v1/api/jobs/{country_code}/search/1"

        # Start with required params
        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "results_per_page": str(limit),
            "sort_by": sort_by.lower()
        }

        # Only include job type flags if selected (1)
        if full_time:
            params["full_time"] = "1"
        if part_time:
            params["part_time"] = "1"
        if contract:
            params["contract"] = "1"
        if permanent:
            params["permanent"] = "1"


        # Add location if provided
        if location:
            params["where"] = location

        # Make the request
        response = requests.get(base_url, params=params)

        # Debug info
        print("Request URL:", response.url)
        print("Status code:", response.status_code)
        print("Response snippet:", response.text[:500])

        if response.status_code != 200:
            print("Error fetching jobs")
            return []

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON. Raw response:")
            print(response.text[:500])
            return []

        return data
    
    @staticmethod
    def streamlit_format(data):
        jobs = data.get("results", [])

        formatted_jobs = []

        for job in jobs:
            formatted_jobs.append({
                "Title": job.get("title"),
                "Company": job.get("company", {}).get("display_name"),
                "Location": job.get("location", {}).get("display_name"),
                "Salary Min": job.get("salary_min") or "N/A",
                "Salary Max": job.get("salary_max") or "N/A",
                "Category": job.get("category", {}).get("label"),
                "Created": job.get("created"),
                "Redirect URL": job.get("redirect_url")
            })

        return formatted_jobs