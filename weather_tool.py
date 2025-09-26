import os                          # For reading API keys from environment variables
import requests                   # For sending HTTP requests
from dotenv import load_dotenv   # To load .env file

load_dotenv()  # Load environment variables from .env file

def get_weather(location):
    api_key = os.getenv("OPENWEATHER_API_KEY")  # 🔐 Load your OpenWeatherMap API key
    url = "https://api.openweathermap.org/data/2.5/weather"  # 🌐 API endpoint

    # 📦 Define the request parameters
    params = {
        "q": location,         # Search query (e.g., Phnom Penh)
        "appid": api_key,      # API key from your .env file
        "units": "metric"      # Get temperature in Celsius
    }

    # 📡 Make the GET request to the API
    response = requests.get(url, params=params)

    # 🧠 Convert the response to a dictionary (very important!)
    data = response.json()

    # ✅ If request is successful
    if response.status_code == 200:
        temp = data["main"]["temp"]                       # 🌡️ Extract temperature
        desc = data["weather"][0]["description"]          # 🌤️ Weather description
        return f"The weather in {location} is {desc} with a temperature of {temp}°C."

    # ❌ If something goes wrong
    else:
        return f"Could not retrieve weather data for {location}. Reason: {data.get('message', 'Unknown error')}."
