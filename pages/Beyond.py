import streamlit as st
import backend
import datetime

st.set_page_config(layout = 'wide')

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(
    f"""<h1 style='
        color: black; 
        font-family: "Orbitron", sans-serif;
        font-size: 90px; 
        text-align: center;
        '>ABOVE & BEYOND</h1>""", 
        unsafe_allow_html=True)

st.header("Beyond: Astronomy Image of the Day for the Past Days")

days = st.slider("Past Days", min_value=1, max_value=5, key="days", help="Select the number of forecasted days")

API_KEY = st.secrets("NASA")

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