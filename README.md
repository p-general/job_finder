# Job Scraper Automation Tool

## Project Structure

job-finder/
├── db.py               # Initializes the SQL schema and handles database connections
├── job_fetch.py        # Fetches raw job postings from Adzuna
├── job_parse.py        # Cleans and normalizes data and inserts it into SQL
├── pipeline.py         # Orchestrates the pipeline: fetch → parse → SQL
├── streamlit_app.py    # Launches the Streamlit dashboard
├── database/
│   ├── schema.sql      # Database schema for reproducibility
│   └── sample_jobs.db  # Small sample dataset for demonstration
├── requirements.txt
└── README.md


## Overview
A Python automation tool that scrapes job postings using the Adzuna Job API, cleans the data, and exports structured results into SQLite for analysis or visualization in a Streamlit dashboard. This project demonstrates web automation, data pipelines, and internal-style productivity tools.

## Why I Built This
I wanted hands-on experience with web automation, data pipelines, and
building internal-style tools that reduce repetitive manual work.

## Features
- Fetches job postings via the Adzuna Job API

- Normalizes and cleans raw text data

- Inserts structured data into SQLite

- Streamlit dashboard for exploring and filtering jobs

- Configurable search filters (location, role, keywords)

- Download all results as CSV

## Tech Stack
- Python 3.x
- requests / BeautifulSoup
- pandas
- Streamlit
- SQLite


## How to run
- Clone Repository: git clone https://github.com/p-general/job-finder.git
- Install Dependencies: pip install -r requirements.txt
- Run the database initialization (optional if you want a fresh DB): python db.py
- Run the full pipeline to fetch and insert jobs: python pipeline.py
- Launch the Streamlit Dashboard: streamlit run streamlit_app.py

A small sample database (database/sample_jobs.db) is included with public job postings from Adzuna.

The database is included for demonstration purposes only.

The pipeline can generate a fresh database dynamically.
 
