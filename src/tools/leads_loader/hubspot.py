import os
import hubspot
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException
from .lead_loader_base import LeadLoaderBase


class HubSpotLeadLoader(LeadLoaderBase):
    def __init__(self):
        self.client = hubspot.Client.create(access_token=os.getenv("HUBSPOT_API_KEY"))

    def fetch_records(self, status_filter="NEW"):
        try:
            api_response = self.client.crm.contacts.basic_api.get_page(
                limit=100,
                properties=["email", "firstname", "lastname", "hs_lead_status"],
                archived=False,
            )
            records = []
            for contact in api_response.results:
                lead_status = contact.properties.get("hs_lead_status")
                if lead_status == status_filter:
                    records.append({
                        "id": contact.id,
                        "name": f"{contact.properties.get('firstname', '')} {contact.properties.get('lastname', '')}",
                        "email": contact.properties.get("email"),
                    })
            return records
        except ApiException as e:
            print(f"Error fetching records from HubSpot: {e}")
            return []

    def update_record(self, lead_id, fields_to_update):
        try:
            # Prepare the fields to update in HubSpot
            properties = fields_to_update
            simple_public_object_input = SimplePublicObjectInput(properties=properties)
            
            # Update the record in HubSpot
            self.client.crm.contacts.basic_api.update(
                contact_id=lead_id, simple_public_object_input=simple_public_object_input
            )
            return {"lead_id": lead_id, "updated_fields": fields_to_update}
        except ApiException as e:
            print(f"Error updating HubSpot record: {e}")
            return None

