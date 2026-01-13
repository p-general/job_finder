import sys
import os
import pandas as pd
import math

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


sort_by = st.selectbox("Sort by", ["Date", "Salary", "Relevance"])

limit = st.slider("Number of jobs to fetch", 10, 250, 100)

selected_job_type = st.radio("Select Job Type", job_types)

full_time = part_time = contract = permanent = 0
if selected_job_type == "Full-time":
    full_time = 1
elif selected_job_type == "Part-time":
    part_time = 1
elif selected_job_type == "Contract":
    contract = 1
elif selected_job_type == "Permanent":
    permanent = 1


# Initialize session state
if "jobs" not in st.session_state:
    st.session_state.jobs = []
if "page" not in st.session_state:
    st.session_state.page = 0

# --- FETCH JOBS ---
if st.button("Fetch Jobs"):
    user = client.Job_Finder()
    jobs = user.job_fetcher(
        country_code=selected_country_code,
        limit=limit,
        sort_by=sort_by,
        full_time=full_time,
        part_time=part_time,
        contract=contract,
        permanent=permanent,
        location=None
    )
    st.session_state.jobs = jobs
    st.session_state.page = 0  # reset to first page

# --- DISPLAY JOBS WITH PAGINATION ---
jobs = st.session_state.jobs
if len(jobs) > 0:
    jobs_per_page = 10
    total_pages = max(1, math.ceil(len(jobs) / jobs_per_page))
    start_idx = st.session_state.page * jobs_per_page
    end_idx = start_idx + jobs_per_page
    jobs_to_display = jobs[start_idx:end_idx]

    # Display jobs
    for job in jobs_to_display:
        st.markdown(
            f"**{job['Title']}** at {job['Company']} — {job['Location']}  \n"
            f"Salary: {job['Salary Min']} - {job['Salary Max']}  \n"
            f"[Apply Here]({job['Redirect URL']})"
        )
        st.markdown("---")

    # Pagination buttons
    col1, col2, col3 = st.columns([1, 1, 6])

    with col1:
        if st.button("Previous"):
            if st.session_state.page > 0:
                st.session_state.page -= 1

    with col2:
        if st.button("Next"):
            if st.session_state.page < total_pages - 1:
                st.session_state.page += 1

    with col3:
        st.write(f"Page {st.session_state.page + 1} of {total_pages}")
else:
    st.info("No jobs to display. Click 'Fetch Jobs' to load jobs.")


