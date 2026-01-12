import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

SKILL_MAP = {
    "soft_skills": [
        "Collaboration",
        "Teamwork",
        "Communication",
        "Problem Solving",
        "Critical Thinking",
        "Attention to Detail",
        "Time Management",
        "Adaptability",
        "Leadership",
        "Professional Development",
        "Continuous Learning",
        "Customer Service",
        "Conflict Resolution",
        "Decision Making",
        "Organization",
        "Multitasking"
    ],

    "tools_and_software": [
        "Excel",
        "Word",
        "PowerPoint",
        "Google Sheets",
        "Google Docs",
        "Outlook",
        "QuickBooks",
        "SAP",
        "CRM",
        "Salesforce",
        "Slack",
        "Zoom",
        "Scheduling Software",
        "Data Entry Systems",
        "POS Systems",
        "Accounting Software"
    ],

    "certifications": [
        "CPA",
        "PMP",
        "OSHA",
        "ServSafe",
        "Forklift Certification",
        "First Aid",
        "CPR",
        "Six Sigma",
        "Project Management Certification"
    ],

    "domain_skills": [
        "Tax Services",
        "Advisory",
        "Audit",
        "Assurance",
        "Financial Analysis",
        "Accounting",
        "Budgeting",
        "Payroll",
        "Inventory Management",
        "Compliance",
        "Quality Control",
        "Logistics",
        "Operations Management",
        "Scheduling",
        "Reporting",
        "Data Analysis",
        "Risk Assessment",
        "Client Relations",
        "Recruitment",
        "Training",
        "Procurement"
    ],

    "physical_or_operational": [
        "Lifting",
        "Warehouse Operations",
        "Equipment Operation",
        "Shift Work",
        "Manual Labor",
        "Stocking",
        "Shipping",
        "Receiving",
        "Inventory Control",
        "Transportation"
    ]
}

cursor.execute("SELECT job_id, title, description FROM jobs")

keywords = []
job_amount = 0
for job_id, title, description in cursor:
    description_lower = description.lower()
    found_skills = set()

    for category, skills in SKILL_MAP.items():
        for skill in skills:
            if skill.lower() in description_lower:
                found_skills.add(skill)
    
    for skill in found_skills:
        cursor.execute(
            "INSERT OR IGNORE INTO skills (job_id, title, skills) VALUES (?, ?, ?)",
            (job_id, title, skill)
        )

conn.commit()
conn.close()

print("Skills parsed")