from db import get_connection

INSERT_JOB_SQL = """
INSERT OR IGNORE INTO jobs (
    job_id, title, company, location, description,
    salary_min, salary_max, contract_type,
    created, url
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""


def input_listing(data):

    con = get_connection()
    cursor = con.cursor()

    new_jobs = 0
    for job in data.get("results", []):
        
        job_record = {
            "job_id": job["id"],
            "title": job["title"].strip(),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "salary_max": job.get("salary_max"),
            "salary_min": job.get("salary_min"),
            "contract_type": job.get("contract_type"),
            "created": job.get("created"),
            "url": job.get("redirect_url")
        }
        cursor.execute(
            INSERT_JOB_SQL,
            (
                job_record["job_id"],
                job_record["title"],
                job_record["company"],
                job_record["location"],
                job_record["description"],
                job_record["salary_min"],
                job_record["salary_max"],
                job_record["contract_type"],
                job_record["created"],
                job_record["url"],
            )
        )
        if cursor.rowcount == 1:
            new_jobs += 1

    con.commit()
    con.close()

    print(f"{new_jobs} Jobs Loaded.")
    return new_jobs
    