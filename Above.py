import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout = 'wide')

st.title("ABOVE & BEYOND")

st.header("Above: Weather Forecast for the Next Days")

place = st.text_input("Place: ", key="place")

days = st.slider("Forecast Days", min_value=1, max_value=5, key="days", help="Select the number of forecasted days")

option = st.selectbox("Select the data to view", ("Temperature", "Sky"), key="option")

st.subheader(f"{st.session_state["option"]} for the next {st.session_state["days"]} days in {st.session_state["place"].title()}")

if place and option and days:
    try:
        filtered_data = get_data(place, days)

        #create a temperature plot if we get temperature option
        if option == "Temperature":
            temperatures = [item['main']['temp'] for item in filtered_data]
            temperatures_f = [((item/10) * (9/5) + 32) for item in temperatures]
            dates = [item['dt_txt'] for item in filtered_data]
            figure = px.line(x=dates, y=temperatures_f, labels={"x": "Date", "y": "Temperature (F)"})
            st.plotly_chart(figure)

        elif option == "Sky":
            skies = [item['weather'][0]['main'] for item in filtered_data]
            print(skies)
            images = []
            for sky in skies:
                if sky == "Clear":
                    images.append("sky_images/clear.png")
                elif sky == "Clouds":
                    images.append("sky_images/cloud.png")
                elif sky == "Rain":
                    images.append("sky_images/rain.png")
                elif sky == "Snow":
                    images.append("sky_images/snow.png")
            st.image(images, width=115)
    except KeyError:
        st.info("That is not a valid city. Please enter an existing city.")

