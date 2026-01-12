import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import streamlit as st
from api import client

country_dict = {
    "United States": "us",
    "United Kingdom": "gb",
    "Austria": "at",
    "Australia": "au",
    "Belgium": "be",
    "Brazil": "br",
    "Canada": "ca",
    "Switzerland": "ch",
    "Germany": "de",
    "Spain": "es",
    "France": "fr",
    "India": "in",
    "Italy": "it",
    "Mexico": "mx",
    "Netherlands": "nl",
    "New Zealand": "nz",
    "Poland": "pl",
    "Singapore": "sg",
    "South Africa": "za"
}

st.title("Interactive Job Query")

# Dropdown with full names
selected_country_name = st.selectbox("Select Country", list(country_dict.keys()))

# Get the API code
selected_country_code = country_dict[selected_country_name]

st.subheader("Select Job Types")

# Job type options
job_types = ["Full-time", "Part-time", "Contract", "Permanent"]
all_option = "All"

# Session state to keep track of selections
if "selected_jobs" not in st.session_state:
    st.session_state.selected_jobs = []

# Checkbox for "All"
all_checked = st.checkbox(all_option, key="all_option", value="All" in st.session_state.selected_jobs)

# If "All" is checked, clear other selections
if all_checked:
    st.session_state.selected_jobs = [all_option]

# Show other job type checkboxes only if "All" is not checked
for job in job_types:
    if not all_checked:
        checked = st.checkbox(job, key=job)
        if checked and job not in st.session_state.selected_jobs:
            st.session_state.selected_jobs.append(job)
        elif not checked and job in st.session_state.selected_jobs:
            st.session_state.selected_jobs.remove(job)



sort_by = st.selectbox("Sort by", ["Default", "Hybrid", "Date", "Salary", "Relevance"])

limit = st.slider("Number of jobs to fetch", 10, 250, 100)

selected = st.session_state.selected_jobs

# Initialize flags
full_time = part_time = contract = permanent = 0

match selected:
    case ["All"]:
        full_time = part_time = contract = permanent = 1
    case ["Full-time"]:
        full_time = 1
    case ["Part-time"]:
        part_time = 1
    case ["Contract"]:
        contract = 1
    case ["Permanent"]:
        permanent = 1


if st.button("Fetch Jobs"):
    location = selected_country_code
    user = client.Job_Finder()
    jobs = user.job_fetcher(location, limit, sort_by, full_time, part_time, contract, permanent)
    st.write(f"Fetched {len(jobs)} jobs")
    st.dataframe(jobs)







