# Job Scraper Automation Tool

## Project Structure

- `db.py` – Initializes the SQL schema and handles database connections
- `job_fetch.py` – Scrapes raw job postings from the web
- `job_parse.py` – Cleans and normalizes scraped data commiting it into the SQL
- `pipeline.py` – Orchestrates the full ingestion process (fetch → parse → SQL)
- `streamlit_app.py` – Launches a Streamlit dashboard that can process new data and download all available jobs into CSV format.

## Overview
A Python automation tool that scrapes job postings using Adzuna job API's,
cleans the data, and exports structured results into an SQL for analysis and or a streamlit website.

## Why I Built This
I wanted hands-on experience with web automation, data pipelines, and
building internal-style tools that reduce repetitive manual work.

## Features
- Scrapes job postings using requests + BeautifulSoup
- Normalizes and cleans raw text data
- Exports results to SQL
- Configurable search filters (location, role, keywords)

## Tech Stack
- Python
- requests / BeautifulSoup
- pandas


## Example Output
See `database/sample.db`
 
