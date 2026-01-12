import sqlite3

db_path = "jobs.db"

def get_connection():
    return sqlite3.connect(db_path)

CREATE_TABLE_SQL_JOBS = """
CREATE TABLE IF NOT EXISTS jobs (
    job_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    company TEXT,
    location TEXT,
    description TEXT,
    salary_min INTEGER,
    salary_max INTEGER,
    contract_type TEXT,
    created DATE,
    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    url TEXT
);
"""

CREATE_TABLE_SQL_SKILLS = """
CREATE TABLE IF NOT EXISTS skills (
    job_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    skills TEXT
);
"""
con = get_connection()
cursor = con.cursor()
cursor.execute(CREATE_TABLE_SQL_SKILLS)
cursor.execute(CREATE_TABLE_SQL_JOBS)
print("Database Created")
con.commit()
con.close()