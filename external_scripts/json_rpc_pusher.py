import json
import requests
import os

url = "http://localhost:8017/jsonrpc"
db = "odoo_db"
username = "admin"
password = "password"

headers = {"Content-Type": "application/json"}

login_payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "common",
        "method": "authenticate",
        "args": [db, username, password, {}],
    },
    "id": 1,
}

login_response = requests.post(url, headers=headers, data=json.dumps(login_payload))
uid = login_response.json().get("result")

if not uid:
    print("Failed to authenticate.")
    exit()

print(f"Authenticated UID: {uid}")


def create_record(model_name, records):
    create_payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "object",
            "method": "execute_kw",
            "args": [
                db,
                uid,
                password,
                model_name,
                "create",
                [records],
            ],
        },
        "id": 2,
    }

    response = requests.post(url, headers=headers, data=json.dumps(create_payload))
    result = response.json()
    print(f"Response from Odoo for '{model_name}': {json.dumps(result, indent=2)}")


# Get base path of this script
base_path = os.path.dirname(os.path.abspath(__file__))

# VentureBeat Page
with open(
    os.path.join(base_path, "venturebeat_about.json"), "r", encoding="utf-8"
) as f:
    page_data = json.load(f)

create_record(
    "scraped.page",
    [
        {
            "title": page_data["title"],
            "content": page_data["content"],
            "source_url": page_data["url"],
        }
    ],
)

# LinkedIn Jobs
with open(os.path.join(base_path, "linkedin_jobs.json"), "r", encoding="utf-8") as f:
    jobs_data = json.load(f)

job_records = []
for job in jobs_data["jobs"]:
    job_records.append(
        {
            "name": job["title"],
            "company_name": job["company"],
            "location": job["location"],
            "date_posted": job["posted_date"],
            "source_url": job["link"],
            "company_logo_url": job.get("company_logo", ""),
        }
    )

create_record("scraped.job", job_records)

# TechCrunch Blogs
with open(
    os.path.join(base_path, "techcrunch_articles_20250518_113258.json"),
    "r",
    encoding="utf-8",
) as f:
    blogs_data = json.load(f)

blog_records = []
for article in blogs_data:
    blog_records.append(
        {
            "title": article["title"],
            "content": article.get("full_content", "") or "",
            "published_date": article.get("published_date", ""),
            "source_url": article["source_url"],
        }
    )

create_record("scraped.blog", blog_records)
