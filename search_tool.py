# Import requests library for making HTTP requests
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def search(query):
    api_key = os.getenv("GOOGLE_API_KEY")  # 🔐 Load your Google API key
    cx = os.getenv("GOOGLE_CX")            # 🔐 Load your Custom Search
    # Base URL of DuckDuckGo's Instant Answer API
    url = "https://www.googleapis.com/customsearch/v1"

    # Parameters to send in the GET request
    params = {
        "key": api_key,     # API key
        "cx": cx,           # Custom search engine ID
        "q": query          # Search query
    }

    # Make a GET request to Google Custom Search API
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        items = data.get("items", [])
        if items:
            return items[0].get("snippet", "No snippet available.")
        else:
            return "No results found."
    else:
        return f"Error: {response.status_code} - {response.text}"