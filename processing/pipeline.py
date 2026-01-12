from api import client
from . import job_extractor
from .job_extractor import input_listing

def update_jobs():
    listings = client.Job_Finder()
    data = listings.job_fetcher()
    return input_listing(data)


if __name__ == "__main__":
    update_jobs()