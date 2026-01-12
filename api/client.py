import requests

class Job_Finder:
    def __init__(self):
        self.app_id = "REDACTED_APP_ID"
        self.app_key = "REDACTED_APP_KEY"

    def job_fetcher(
        self,
        country_code,
        limit=100,
        sort_by="date",
        full_time=0,
        part_time=0,
        contract=0,
        permanent=0,
    ):
        """
        Fetch jobs from Adzuna API.

        Args:
            country_code (str): 2-letter country code ('gb', 'us', etc.)
            limit (int): number of results
            sort_by (str): 'date', 'salary', 'relevance', etc.
            full_time, part_time, contract, permanent (int): 1 or 0
            location (str, optional): city or area
        Returns:
            list of jobs (dictionaries) or empty list if failed
        """
        base_url = f"https://api.adzuna.com/v1/api/jobs/{country_code}/search/1?app_id=REDACTED_APP_ID&app_key=REDACTED_APP_KEY&results_per_page={limit}&sort_by={sort_by}&full_time={full_time}&part_time={part_time}&contract={contract}&permanent={permanent}"

        # Prepare query parameters
        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "results_per_page": limit,
            "sort_by": sort_by.lower(),
            "full_time": str(full_time),
            "part_time": str(part_time),
            "contract": str(contract),
            "permanent": str(permanent),
        }

        # Send the request
        response = requests.get(base_url, params=params)

        # Debug: see what URL is actually requested
        print("Request URL:", response.url)
        print("Status code:", response.status_code)

        if response.status_code != 200:
            print("Error fetching jobs:", response.text[:500])
            return []

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON. Response snippet:")
            print(response.text[:500])
            return []

        # Adzuna API puts jobs under data["results"]
        jobs = data.get("results", [])

        # Convert to a list of dicts suitable for dataframe
        formatted_jobs = []
        for job in jobs:
            formatted_jobs.append({
                "Title": job.get("title"),
                "Company": job.get("company", {}).get("display_name"),
                "Location": job.get("location", {}).get("display_name"),
                "Salary Min": job.get("salary_min"),
                "Salary Max": job.get("salary_max"),
                "Contract Type": job.get("contract_type"),
                "Category": job.get("category", {}).get("label"),
                "Created": job.get("created"),
                "Redirect URL": job.get("redirect_url")
            })

        return formatted_jobs
