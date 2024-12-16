import os
import requests
from src.utils import google_search


def extract_linkedin_url(search_results, is_company):
    """
    Extracts the LinkedIn URL from the search results.
    
    @param search_results: The search results from which to extract the URL.
    @param is_company: Boolean indicating whether to extract a company URL or a person URL.
    @return: The extracted LinkedIn URL or an error message if not found.
    """
    try:
        for result in search_results:
            if is_company and 'linkedin.com/company' in result['link']:
                return result['link']
            elif not is_company and 'linkedin.com/in' in result['link']:
                return result['link']
        return "LinkedIn URL not found."
    except KeyError:
        return "Invalid search results format."

def scrape_linkedin(linkedin_url, is_company):
    """
    Scrapes LinkedIn profile data based on the provided LinkedIn URL.
    
    @param linkedin_url: The LinkedIn URL to scrape.
    @param is_company: Boolean indicating whether to scrape a company profile or a person profile.
    @return: The scraped LinkedIn profile data.
    """
    if is_company:
        url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-linkedinurl"
    else:
        url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

    querystring = {"linkedin_url": linkedin_url}
    headers = {
      "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
      "x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Request failed with status code: {response.status_code}")
        

def search_lead_company(company_name):
    """
    Searches for the company LinkedIn profile based on the company name.
    
    @param company_name: The name of the company to search for.
    @return: A dictionary containing the company profile data or an error message if not found.
    """
    # Find company LinkedIn URL by searching on Google 'LinkedIn {{company_name}}'
    query = f"LinkedIn {company_name}"
    search_results = google_search(query)
    company_linkedin_url = extract_linkedin_url(search_results, True)
    print(company_linkedin_url)

    if not company_linkedin_url:
        return "Company LinkedIn URL not found."

    # Scrape company LinkedIn page
    company_page_content = scrape_linkedin(company_linkedin_url, True)
    if "data" not in company_page_content:
        return "LinkedIn profile not found"
    
    company_profile = company_page_content["data"]
    return {
        "company_name": company_profile.get("company_name", ""),
        "company_description": company_profile.get("description", ""),
        "company_website": company_profile.get("website", ""),
        "company_location": company_profile.get("locations", []),
        "company_industry": company_profile.get("industries", []),
        "company_size": company_profile.get("employee_count", company_profile.get("employee_range", ""))
    }

def search_lead_profile(lead_name, company_name):
    """
    Searches for the lead's LinkedIn profile based on the lead name and company name.
    
    @param lead_name: The name of the lead to search for.
    @param company_name: The name of the company to associate with the lead.
    @return: A dictionary containing the lead profile data or an error message if not found.
    """
    # Find lead LinkedIn URL by searching on Google 'LinkedIn {{lead_name}} {{company_name}}'
    query = f"LinkedIn {lead_name} {company_name}"
    search_results = google_search(query)
    lead_linkedin_url = extract_linkedin_url(search_results, False)
    print(lead_linkedin_url)

    if not lead_linkedin_url:
        return "Lead LinkedIn URL not found."

    # Scrape lead LinkedIn profile
    lead_profile_content = scrape_linkedin(lead_linkedin_url, False)
    if "data" not in lead_profile_content:
        return "LinkedIn profile not found"
    
    lead_profile_content = lead_profile_content["data"]
    return {
        "about": lead_profile_content.get('about', ''),
        "skills": lead_profile_content.get('skills', []),
        "educations": [
            {
                "field_of_study": edu.get('field_of_study', ''),
                "date_range": edu.get('date_range', '')
            } for edu in lead_profile_content.get('educations', [])
        ],
        "experiences": [
            {
                "company": exp.get('company', ''),
                "title": exp.get('title', ''),
                "date_range": exp.get('date_range', ''),
                "is_current": exp.get('is_current', False),
                "location": exp.get('location', ''),
                "description": exp.get('description', '')
            } for exp in lead_profile_content.get('experiences', [])
        ]
    }