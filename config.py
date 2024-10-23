import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY")
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 300  # 5 minutes
TEMPERATURE_UNIT = "Celsius"  # or "Fahrenheit"
