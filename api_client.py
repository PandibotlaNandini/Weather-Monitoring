import requests
from config import API_KEY, API_BASE_URL

def get_weather_data(city):
    params = {"q": city, "appid": API_KEY}
    response = requests.get(API_BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
