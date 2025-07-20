import streamlit as st
import backend
import datetime
import os

st.set_page_config(layout = 'wide')

st.title("ABOVE & BEYOND")

st.header("Beyond: Astronomy Image of the Day for the Past Days")

days = st.slider("Past Days", min_value=1, max_value=5, key="days", help="Select the number of forecasted days")

API_KEY = os.getenv("NASA")

num_days = days

end = datetime.date.today()
start = end - datetime.timedelta(days=num_days - 1)

astronomy_url = f"https://api.nasa.gov/planetary/apod?start_date={start}&end_date={end}&api_key={API_KEY}"

backend.get_image(astronomy_url, days)

desc_list = backend.get_description(astronomy_url)
dates = backend.get_dates(astronomy_url)

for i in range(days):
    st.subheader(dates[i])
    st.image(f"astronomy_images/image{i}.jpg")
    st.text(desc_list[i])