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
        

# def search_lead_company(company_name):
#     """
#     Searches for the company LinkedIn profile based on the company name.
    
#     @param company_name: The name of the company to search for.
#     @return: A dictionary containing the company profile data or an error message if not found.
#     """
#     # Find company LinkedIn URL by searching on Google 'LinkedIn {{company_name}}'
#     query = f"LinkedIn {company_name}"
#     search_results = google_search(query)
#     company_linkedin_url = extract_linkedin_url(search_results, True)
#     print(company_linkedin_url)

#     if not company_linkedin_url:
#         return "Company LinkedIn URL not found."

#     # Scrape company LinkedIn page
#     company_page_content = scrape_linkedin(company_linkedin_url, True)
#     if "data" not in company_page_content:
#         return "LinkedIn profile not found"
    
#     company_profile = company_page_content["data"]
#     return {
#         "company_name": company_profile.get("company_name", ""),
#         "company_description": company_profile.get("description", ""),
#         "company_website": company_profile.get("website", ""),
#         "company_location": company_profile.get("locations", []),
#         "company_industry": company_profile.get("industries", []),
#         "company_size": company_profile.get("employee_count", company_profile.get("employee_range", ""))
#     }

# def search_lead_profile(lead_name, company_name):
#     """
#     Searches for the lead's LinkedIn profile based on the lead name and company name.
    
#     @param lead_name: The name of the lead to search for.
#     @param company_name: The name of the company to associate with the lead.
#     @return: A dictionary containing the lead profile data or an error message if not found.
#     """
#     # Find lead LinkedIn URL by searching on Google 'LinkedIn {{lead_name}} {{company_name}}'
#     query = f"LinkedIn {lead_name} {company_name}"
#     search_results = google_search(query)
#     lead_linkedin_url = extract_linkedin_url(search_results, False)
#     print(lead_linkedin_url)

#     if not lead_linkedin_url:
#         return "Lead LinkedIn URL not found."

#     # Scrape lead LinkedIn profile
#     lead_profile_content = scrape_linkedin(lead_linkedin_url, False)
#     if "data" not in lead_profile_content:
#         return "LinkedIn profile not found"
    
#     lead_profile_content = lead_profile_content["data"]
#     return {
#         "about": lead_profile_content.get('about', ''),
#         "skills": lead_profile_content.get('skills', []),
#         "educations": [
#             {
#                 "field_of_study": edu.get('field_of_study', ''),
#                 "date_range": edu.get('date_range', '')
#             } for edu in lead_profile_content.get('educations', [])
#         ],
#         "experiences": [
#             {
#                 "company": exp.get('company', ''),
#                 "title": exp.get('title', ''),
#                 "date_range": exp.get('date_range', ''),
#                 "is_current": exp.get('is_current', False),
#                 "location": exp.get('location', ''),
#                 "description": exp.get('description', '')
#             } for exp in lead_profile_content.get('experiences', [])
#         ]
#     }


def search_lead_company(company_name):
    return {
        "company_name": "Relevance AI",
        "company_description": "At Relevance AI, our mission is to be the home of the AI workforce. Our no-code platform enables anyone to build AI teams, equipped with custom AI tools.",
        "company_website": "https://relevanceai.com",
        "company_location": [
            {
                "city": "San Francisco",
                "country": "US",
                "full_address": "San Francisco, California, US",
                "is_headquarter": "false",
                "line1": "",
                "line2": "",
                "region": "California",
                "zipcode": ""
            },
            {
                "city": "Surry Hills",
                "country": "AU",
                "full_address": "132 Kippax St, Surry Hills, New South Wales 2010, AU",
                "is_headquarter": "true",
                "line1": "132 Kippax St",
                "line2": "",
                "region": "New South Wales",
                "zipcode": "2010"
            }
        ],
        "company_industry": [
            "Software Development"
        ],
        "company_size": 52
    }

def search_lead_profile(lead_name, company_name):
    return {
        "about": "At Relevance AI, we believe the future of human prosperity lies in AI technology. Our mission is to be the home of the modern AI workforce, enabling organizations to create autonomous AI Agents that can perform entire roles previously dependent on humans. \n\nFrom automating common roles like Sales Development Representatives to specialized roles integrated with proprietary systems, Relevance AI empowers organizations to 'hire' their first AI employees and build their AI workforce.\n\nBy leveraging an AI Workforce, organizations can decouple the traditionally linear relationship between business growth and headcount.",
        "skills": [],
        "educations": [
            {
                "field_of_study": "Entrepreneurship/Global business/Strategic planning",
                "date_range": "2018 - 2019"
            },
            {
                "field_of_study": "Strategy management and Innovation",
                "date_range": "2017 - 2019"
            },
            {
                "field_of_study": "Engineering",
                "date_range": "2013 - 2017"
            },
            {
                "field_of_study": "",
                "date_range": "2009 - 2013"
            }
        ],
        "experiences": [
            {
                "company": "Relevance AI",
                "title": "Growth Operations Lead",
                "date_range": "Aug 2021 - Present",
                "is_current": "true",
                "location": "Budapest, Hungary",
                "description": "Relevance AI is the home of the AI Workforce. Enabling anyone to build autonomous AI teams and put their processes on true autopilot.\n\nOur first flagship AI employee, an autonomous AI BDR, delivers 10-15 sales-accepted meetings to your inbox weekly, on autopilot. Working 24/7, it conducts in-depth research, sends hyper-personalised emails, handles any questions and objections, and arranges meetings with a detailed handover to your sales team."
            },
            {
                "company": "RAMI Fashion",
                "title": "Business Partner I Advisor",
                "date_range": "Nov 2020 - Present",
                "is_current": "true",
                "location": "",
                "description": "Featured in Hungarian Shark Tank. Raised over $75k from investors. Now looking to achieve sustainable growth."
            },
            {
                "company": "Kindly",
                "title": "BizOps Lead & Co-founder",
                "date_range": "Jan 2022 - Jun 2022",
                "is_current": "false",
                "location": "",
                "description": "Kindly is a digital bank, bridging the gap between personal finances and a more sustainable and progressive world \ud83c\udf0e"
            },
            {
                "company": "Intland Software",
                "title": "Sales Operations Manager",
                "date_range": "Oct 2020 - Aug 2021",
                "is_current": "false",
                "location": "Stuttgart Region",
                "description": "- Designing and implementing scalable and repeatable sales and marketing processes to enable the company to grow more than 30 % YoY, crossing the chasm. \n- Supporting Sales and Marketing Management in executing the 2021 Go To Market Strategy."
            },
            {
                "company": "Deloitte Hungary",
                "title": "Management Consultant I Strategy and Operations",
                "date_range": "Oct 2019 - Oct 2020",
                "is_current": "false",
                "location": "Hungary",
                "description": "Executing on Senior Consultant / Manager responsibilities, consulted companies with challenges in strategy and operations."
            },
            {
                "company": "EasyPark Group",
                "title": "Market Research Analyst I Business Developement",
                "date_range": "Mar 2018 - Jun 2019",
                "is_current": "false",
                "location": "Copenhagen Area, Denmark",
                "description": "- Organized and conducted a robust market research and analysis of 90+ countries resulting in major amendments of the company\u2019s global strategy.\n- Designed and improved research and partnership assessment frameworks resulting in more efficient evaluation processes for potential new market entry.\n- Developed and presented business cases for entering new countries that led to a successful company acquisition in Reykjav\u00edk, Iceland and greenfield market entry in the Faroe Islands.\n- Conducted a detailed research of the Hungarian parking market, built relationships with leading Hungarian mobile paid parking providers. Organized mergers and acquisitions (M&A) negotiations with selected provider supporting Hungarian market entry decision of the management board."
            },
            {
                "company": "Copenhagen School of Entrepreneurship",
                "title": "Business developer & Partner at TAG I CSE startup incubator",
                "date_range": "Nov 2017 - Jun 2018",
                "is_current": "false",
                "location": "Copenhagen, Capital Region, Denmark",
                "description": "As an incubated startup at CSE we developed an e-commerce application to help creators and influencers monetize their content.\n\n\"Imagine Instagram, but with the swipe of your finger you can see all products tagged on the picture with affiliate links directing you to the store where you can buy them.\""
            },
            {
                "company": "AAM Management Information Consulting Ltd.",
                "title": "Management Consultant I IT &\u00a0technology services",
                "date_range": "Oct 2016 - Jul 2017",
                "is_current": "false",
                "location": "Budapest, Hungary",
                "description": "Specializing in IT project management. \n- Implemented agile project management practices in scrum at a Hungarian fintech spinoff company (OTP eBIZ) organizing day to day operations, resulting in a successful minimum viable product (MVP) launch achieved on quality, on time and on budget.\n- As a leader of a team of 5 at OTP eBIZ, established structured test management operations leading to faster, more efficient subsequent product launches.\n- Led the establishment and maturation of a project organization at OTP eBIZ resulting in the scale-up of the company from 20 to 35 people within 5 months.\n- Designed and implemented a new process for internal project pipeline at E.ON resulting in more efficient software development life cycles ultimately cutting significant costs associated with internal IT projects."
            },
            {
                "company": "Camp Leaders",
                "title": "Camp Counselor",
                "date_range": "May 2016 - Aug 2016",
                "is_current": "false",
                "location": "Portland, Maine Area",
                "description": ""
            },
            {
                "company": "MVM OVIT Zrt.",
                "title": "Project Management Specialist",
                "date_range": "Feb 2016 - Apr 2016",
                "is_current": "false",
                "location": "Budapest, Hungary",
                "description": "- Provided administrative assistance to the project manager of an international project in Jordan with the approximate budget of $20 MM.\n- Delegated tasks to project members based on high quality, detailed memorandums from project meetings leading to more organized and effective project work.\n- Gathered and analyzed financial information, created reports to the project manager achieving a more efficient budget controlling."
            },
            {
                "company": "Crowd Mobile",
                "title": "Research Analyst Intern",
                "date_range": "Jun 2015 - Sep 2015",
                "is_current": "false",
                "location": "Budapest, Hungary",
                "description": "Crowd Mobile is a global mobile entertainment and digital media company from Australia specialized in mobile products and digital marketing.\n- Being part of the customer service team, established and managed customer relationship.\n- Excelled in fast research providing information and solutions to customers, maintaining and improving the overall customer satisfaction."
            }
        ]
    }