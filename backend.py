import requests
import streamlit as st

API_KEY = st.secrets["FORECASTING"]

def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    filtered_data_with_days = filtered_data[:(8 * days)]
    return filtered_data_with_days


def get_image(url, days):
    response = requests.get(url)

    content = response.json()

    num_images = days
    file_numbers = []
    for num in range(num_images):
        file_numbers.append(num)

    index = 0
    for item in content:
        image_url = item['url']
        image_response = requests.get(image_url)
        with open(f"astronomy_images/image{index}.jpg", "wb") as file:
            file.write(image_response.content)
        index += 1



def get_description(url):
    response = requests.get(url)

    content = response.json()

    desc_list = []
    for item in content:
        desc = item['explanation']
        desc_list.append(desc)

    return desc_list



def get_dates(url):
    response = requests.get(url)

    content = response.json()

    dates = []
    for item in content:
        date = item['date']
        dates.append(date)

    return dates


