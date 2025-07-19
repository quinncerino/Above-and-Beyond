import requests
import os

API_KEY = os.getenv("FORECASTING")

url = f"http://api.openweathermap.org/data/2.5/forecast?q=Paris&appid={API_KEY}"
response = requests.get(url)
data = response.json()
print(data)