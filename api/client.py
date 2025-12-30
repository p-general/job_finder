import requests
import sys

class Job_Finder:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def job_fetcher(self, location="us", query="any", limit="20"):
        self.base_url = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={self.app_id}&app_key={self.app_key}&results_per_page={limit}&what={query}&content-type=application/json"
        params = {
            "location": location,
            "query": query,
            "limit": limit,
            "app_id": self.app_id,
            "app_key": self.app_key

        }     

        response = requests.get(self.base_url)
        data = response.json()

        for job in data.get("results", []):
            print(job.get("title"))
            print(job.get("description"))
            print("-" * 30)
        

test = Job_Finder("REDACTED_APP_ID", "REDACTED_APP_KEY")
test.job_fetcher()

       