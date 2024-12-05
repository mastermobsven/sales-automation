import os
import json
import requests
from litellm import completion
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Set the scopes for Google API
SCOPES = [
    # For using GMAIL API
    'https://www.googleapis.com/auth/gmail.modify',
    # For using Google sheets as CRM, can comment if using Airtable or other CRM
    'https://www.googleapis.com/auth/spreadsheets',
    # For saving files into Google Docs
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive"
]


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def extract_company_name(email):
    """
    Extracts the company name from a professional email address.
    """
    try:
        # Split the email to get the domain part
        company_name = email.split('@')[1]
        return company_name
    except IndexError:
        return "Company not found"
    
    
def get_google_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def google_search(query):
    """
    Performs a Google search using the provided query.
    """
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json().get('organic', [])
    return results

def invoke_llm(system_prompt, user_message, model, response_format=None, json_output=False):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    response = completion(
        model=model,
        messages=messages,
        temperature=0.1,
        response_format=response_format
    )
    output = response.choices[0].message.content
    
    if json_output:
        return json.loads(output)
    return output

def get_report(reports, report_name: str):
    """
    Retrieves the content of a report by its title.
    """
    for report in reports:
        if report.title == report_name:
            return report.content
    return ""

def save_reports_locally(reports):
    # Define the local folder path
    reports_folder = "reports"
    
    # Create folder if it does not exist
    if not os.path.exists(reports_folder):
        os.makedirs(reports_folder)
    
    # Save each report as a file in the folder
    for report in reports:
        file_path = os.path.join(reports_folder, f"{report.title}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(report.content)
