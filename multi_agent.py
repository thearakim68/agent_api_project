# Import all the API tools
from search_tool import search
from calendar_tool import create_event
from weather_tool import get_weather

# Simulate a search task
print("Search results:", search("Cambodia economy 2025"))

# Simulate a weather check task
print("Weather info:", get_weather("Phnom Penh"))

# Simulate scheduling a calendar event
print("Event:", create_event("UX Workshop", "2025-10-27 10:00 AM"))