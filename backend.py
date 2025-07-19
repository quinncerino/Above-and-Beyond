import requests
import os

API_KEY = os.getenv("FORECASTING")

def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    filtered_data_with_days = filtered_data[:(8 * days)]
    return filtered_data_with_days