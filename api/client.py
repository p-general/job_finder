import requests

class JobAPIClient:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.base_url = "https://insert.com"

    def fetch_jobs(self, query="python", location="us", limit=20):
        params = {
            "query": query,
            "location": location,
            "limit": limit
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()