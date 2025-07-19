import streamlit as st
import plotly.express as px

st.set_page_config(layout = 'wide')

st.title("ABOVE & BEYOND")

st.header("Above: Weather Forecast for the Next Days")

place = st.text_input("Place: ", key="place")

days = st.slider("Forecast Days", min_value=1, max_value=5, key="days", help="Select the number of forecasted days")

option = st.selectbox("Select the data to view", ("Temperature", "Sky"), key="option")

st.subheader(f"{st.session_state["option"]} for the next {st.session_state["days"]} days in {st.session_state["place"].title()}")
