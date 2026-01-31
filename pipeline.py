from job_fetch import Job_Finder
from job_parse import input_listing
from db import init_db

def run_pipeline():
    """Full ETL pipeline: fetch jobs → parse → insert into SQL."""
    # 1. Initialize database
    init_db()

    # 2. Fetch raw data
    fetcher = Job_Finder()      
    raw_data = fetcher.job_fetcher()

    # 3. Parse / Insert into DB
    input_listing(raw_data)


if __name__ == "__main__":
    run_pipeline()
