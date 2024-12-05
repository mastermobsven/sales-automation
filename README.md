# AI-Sales-Outreach-Automation

I built an **AI-powered outreach system** designed to integrate with multiple **CRMs**, automate lead research, and enhance the lead generation process. The system analyzes **LinkedIn data**, company websites, recent news, and social media activities to gather comprehensive insights on potential leads. Based on this information, it generates detailed **analysis reports** that highlight lead challenges, gaps, and opportunities for engagement.

The system also creates customized **outreach materials**, including **personalized emails**, **interview preparation scripts**, and **tailored outreach reports** that showcase how our solutions can address the lead's pain points, supported by previous results and case studies.

For this project, I created a sample AI marketing agency, **ElevateAI Marketing Solutions**, which focuses on optimizing and automating content strategies and enhancing digital presence using AI.

While designed for **ElevateAI**, this system can easily be adapted for any agency or freelancer looking to streamline their lead outreach and improve engagement with prospects. With its customizable features, it offers a powerful, automated approach to lead generation.

## Features

### **Multi-CRM Integration**
- Seamlessly connect with popular CRMs like **HubSpot**, **Airtable**, **Google Sheets**, or add your own custom CRM functionality using a standardized schema.

### **Automated Lead Research**
- **Scrape LinkedIn Profile**: Automatically gather key information from LinkedIn to build a complete lead profile.
- **Review Company Website**: Analyze the company’s website for relevant insights about its products, services, and overall digital presence.
- **Analyze Company Digital Presence**: Evaluate the company’s owned blogs and social media activities across platforms like **Facebook**, **Twitter**, **YouTube**, and more.
- **Analyze Recent Company News**: Stay updated with the latest news and announcements about the company, giving you insights into their current initiatives and challenges.
- **Pain Point Identification**: Detect potential challenges or gaps faced by the company to better align your offerings.
- **Report Generation**: For each analysis, generate detailed reports saved locally and in **Google Docs**. A final global research report is created, combining insights from the lead profile, company profile, and digital presence. (You can see example of reports generated in the `/reports` folder)

### **Lead Qualification**
Automatically assess and qualify leads into "qualified" or "not qualified" based on the gathered data and these criteria:
- **Digital Presence (Website & Blog)**: Evaluate the quality and relevance of the company’s online presence.
- **Social Media Activity**: Analyze the company’s engagement and activity across various social media platforms.
- **Industry Fit**: Assess how well the company aligns with your target industries and their current or potential use of **AI** and **automation** in marketing.
- **Company Scale and Potential**: Evaluate the company’s size, growth potential, and market expansion indicators such as new hires or funding.
- **Existing Marketing Strategy**: Understand the company’s current marketing approach to identify areas where your solutions can provide value.

*Note: These criteria can be modified according to specific requirements.*

### **Personalized Outreach**
- **Outreach Report**: Generate a customized outreach report for each lead, highlighting their challenges or gaps, how your services can address them, and referencing previously obtained results and similar case studies (uses RAG to extract them). The report is saved to **Google Docs** for easy sharing.
- **Create Personalized Email**: Craft personalized email templates, including a link to the custom outreach report, to engage qualified leads effectively.
- **Prepare Personalized Interview Script**: Generate a tailored interview script, complete with **SPIN** questions, to help prepare for calls with leads and ensure productive conversations.

### **Efficient Workflow**
- **Seamless Collaboration**: Save all research and outreach materials both locally and in **Google Docs**, ensuring easy access and collaboration across teams.
- **Automated CRM Updates**: Keep your CRM up to date with the latest lead status and links to generated reports, streamlining your outreach efforts.

## System Workflow

The system follows a streamlined and automated process to manage lead research and outreach efficiently (check the complete worflow diagram [here]()):

1. **Fetch Leads**:
   - Connect to your CRM to fetch new leads.
   - The system checks for remaining leads in the CRM.

2. **Research & Insights**:
   - Gather and analyze key information for each lead:
     - Scrape **LinkedIn profiles**.
     - Review the **company website**.
     - Analyze **company digital presence** (blogs, social media, recent news).
   - Generate detailed **digital presence reports** for each lead and company, combining insights from all previous analyses. (see example of reports in the `/reports` folder).

3. **Lead Qualification**:
   - Evaluate each lead based on specific criteria such as **digital presence**, **social media activity**, **industry fit**, and **company scale**.
   - Categorize leads as **qualified** or **not qualified** based on these assessments.

4. **Outreach Preparation**:
   - For qualified leads, generate personalized outreach materials:
     - A **customized outreach report** detailing challenges and how our services can address them, using RAG to fetch similar case studies to be referenced in the report.
     - A **personalized email** with a link to the outreach report.
     - A **customized interview script** to prepare for calls with leads.

5. **Update CRM**:
   - Save all research reports and outreach materials to **Google Docs** and update the CRM with the latest lead status.
   - The system then loops back to check for the next lead to process.


## Advantages of This System

- **Automated and Thorough Lead Research & Qualification**: The system automates the entire lead research process, gathering insights from multiple sources including LinkedIn, company websites, social media, and news. This ensures that no lead is overlooked, and each one is fully assessed based on a set of well-defined criteria

- **Custom Outreach Report**: This system generates detailed, custom outreach reports for each lead. These reports demonstrate that your team has conducted a deep investigation into the lead’s business, clearly indicating how your services can address their specific challenges. By referencing your previous results and relevant case studies, this will strengthen the credibility of your outreach, significantly improving the chances of a positive response.

- **Increased Outreach Reply Rates & Conversions**: By showcasing your expertise and providing value through a tailored report, the system makes your outreach more relevant and compelling. Leads are more likely to respond positively when they see that you understand their business and can offer a tailored solution backed by proof of past success.

- **Scalable, Efficient, and Time-Saving**: The system allows you to handle an increasing number of leads without compromising on quality or research depth. By automating time-consuming tasks like lead research, report generation, and CRM updates, it reduces manual effort and accelerates the process. 

- **Enhanced Collaboration**: With all research and outreach materials saved to Google Docs, your team can easily collaborate on lead strategies, share insights, and refine outreach tactics, making the process even more efficient.

## Integration with APIs

- **Airtable CRM**: To integrate with your Airtable contacts CRM, you must [sign up](https://www.airtable.com/) for an Airtable account and create your own contacts database with the relevant fields.
- **HubSpot CRM**: To integrate with your HubSpot contacts CRM, sign up for a [HubSpot account](https://www.hubspot.com/), then create a private app and obtain your API key. [Follow this tutorial](https://www.youtube.com/watch?v=hSipSbiwc2s) for guidance.
- **LinkedIn Data**: Scrape profile information using the **RapidAPI LinkedIn Profile Data API**. [Get your API key here](https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-data).
- **Google APIs**: Used to access **Google Docs**, **Google Sheets** (needed only when used as CRM source), and **Gmail**. Follow [this guide](https://developers.google.com/gmail/api/quickstart/python) and ensure all required APIs are enabled.
- **Google Searches**: Perform web searches using the **Serper API**. [Get your API key here](https://serper.dev).
- **LLM**: Leverages **Google Gemini LLM models** (Flash and Pro) and their Embedding model. [Get your API key here](https://ai.google.dev/gemini-api/docs/api-key).

## Tech Stack

- **[Langchain](https://python.langchain.com/docs/introduction/)**: Framework for interacting with LLMs and building AI agents and RAG applications.
- **[Langgraph](https://langchain-ai.github.io/langgraph/)**: Framework for building AI agents and automation workflows.
- **[Litellm](https://www.litellm.ai/)**: Easily integrates with multiple LLMs like GPT-4, Gemini, LLAMA3 using a unified structure.

## How to Run

### Prerequisites

- Python 3.9+
- Google Gemini API key (or choose other LLM providers like OpenAI or Groq).
- Google APIs credentials.
- API keys for integrated tools (RapidAPI, Serper API).
- API keys and configurations for your chosen CRM (check `.env.example` for more information).
- Necessary Python libraries (listed in `requirements.txt`).

### Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/kaymen99/sales-outreach-automation-langgraph.git
   cd sales-outreach-automation-langgraph
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a copy of the `.env.example` file:

   ```bash
   cp .env.example .env
   ```

   After running this command, open the new `.env` file and add your API keys as needed.

---

### Start the Application

Run the main script to begin automation:

```sh
python main.py
```

The system will connect with your CRM to fetch new leads, perform automated research, qualify leads, and generate personalized outreach materials (You can see example of reports generated, including the personalized email in the `/reports` folder).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you’d like to see.

## Contact

For questions or suggestions, contact me at `aymenMir1001@gmail.com`.