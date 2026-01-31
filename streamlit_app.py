import pandas as pd
import math
import streamlit as st
from job_fetch import Job_Finder

# -----------------------
# Session state defaults
# -----------------------
if "jobs" not in st.session_state:
    st.session_state.jobs = []
if "page" not in st.session_state:
    st.session_state.page = 0

# -----------------------
# Country selection
# -----------------------
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
selected_country_name = st.selectbox("Select Country", list(country_dict.keys()))
selected_country_code = country_dict[selected_country_name]

# -----------------------
# Job filters
# -----------------------
st.subheader("Select Job Types")
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

# -----------------------
# Fetch jobs
# -----------------------
if st.button("Fetch Jobs"):
    user = Job_Finder()
    raw_jobs = user.job_fetcher(
        country_code=selected_country_code,
        limit=limit,
        sort_by=sort_by,
        full_time=full_time,
        part_time=part_time,
        contract=contract,
        permanent=permanent,
        location=None
    )
    # Convert to human-readable format for Streamlit
    st.session_state.jobs = user.streamlit_format(raw_jobs)
    st.session_state.page = 0  # reset page on new fetch

# -----------------------
# Display jobs with pagination
# -----------------------
jobs = st.session_state.jobs

if jobs:
    jobs_per_page = 10
    total_pages = max(1, math.ceil(len(jobs) / jobs_per_page))

    # Clamp page in case total_pages shrank
    st.session_state.page = max(0, min(st.session_state.page, total_pages - 1))

    # Jump to page input
    jump_page = st.number_input(
        "Jump to page",
        min_value=1,
        max_value=total_pages,
        value=st.session_state.page + 1,
        step=1
    )
    st.session_state.page = jump_page - 1  # zero-indexed internally

    # CSV download
    df = pd.DataFrame(jobs)
    csv = df.to_csv(index=False)
    st.download_button(
        "⬇ Download all jobs as CSV",
        csv,
        "jobs.csv",
        "text/csv"
    )

    # Paginated slice
    start = st.session_state.page * jobs_per_page
    end = start + jobs_per_page
    page_jobs = jobs[start:end]

    # Display jobs
    for job in page_jobs:
        st.markdown(
            f"### {job['Title']}\n"
            f"**{job['Company']}** — {job['Location']}  \n"
            f"Salary: {job['Salary Min']} - {job['Salary Max']}  \n"
            f"[Apply Here]({job['Redirect URL']})"
        )
        st.markdown("---")

    # Pagination buttons
    col1, col2, col3 = st.columns([1, 1, 6])
    with col1:
        if st.button("⬅ Previous", disabled=st.session_state.page == 0):
            st.session_state.page = max(0, st.session_state.page - 1)
    with col2:
        if st.button("Next ➡", disabled=st.session_state.page >= total_pages - 1):
            st.session_state.page = min(total_pages - 1, st.session_state.page + 1)
    with col3:
        st.write(f"Page **{st.session_state.page + 1}** of **{total_pages}**")

else:
    st.info("Click **Fetch Jobs** to load results.")
