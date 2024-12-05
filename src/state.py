from pydantic import BaseModel
from typing import List, Annotated
from typing_extensions import TypedDict
from operator import add
    
class SocialMediaLinks(BaseModel):
    blog: str
    facebook: str
    twitter: str
    youtube: str
    # Can add other platform
    
class Report(BaseModel):
    title: str
    content: str
    is_markdown: bool

class LeadData(BaseModel):
    id: str
    name: str
    email: str
    profile: str

class CompanyData(BaseModel):
    name: str
    profile: str
    website: str
    social_media_links: SocialMediaLinks

class GraphState(TypedDict):
    leads: List[dict]
    lead_data: LeadData
    lead_score: str
    company_data: CompanyData
    reports: Annotated[list[Report], add]
    reports_folder_link: str
    custom_outreach_report_link: str
    personalized_email: str
    interview_script: str
    num_leads: int