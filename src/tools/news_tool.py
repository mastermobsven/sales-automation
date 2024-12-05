import os
import requests
import json

def get_recent_news(company: str) -> str:
    url = "https://google.serper.dev/news"
    
    # Define the payload for the request
    payload = json.dumps({
        "q": company,
        "num": 20,
        "tbs": "qdr:y"
    })
    
    # Set the headers
    headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
    }
    
    # Make the POST request to the API
    response = requests.post(url, headers=headers, data=payload)
    
    # Check if the response is successful
    if response.status_code == 200:
        news = response.json().get("news", [])
        
        # Prepare the string to return
        news_string = ""
        news.reverse()  # Reverse the list to get the most recent news first
        
        for item in news:
            title = item.get('title')
            snippet = item.get('snippet')
            date = item.get('date')
            link = item.get('link')
            
            news_string += f"Title: {title}\nSnippet: {snippet}\nDate: {date}\nURL: {link}\n\n"
        
        return news_string
    else:
        return f"Error fetching news: {response.status_code}"


