import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast')
location = st.text_input("Zip Code: ")
days = st.slider('Forecast by Days', min_value=1, max_value=5,
                 help="Select the number of forecast days")

option = st.selectbox("Select Data to View", ('Graph', 'Sky'))

st.subheader(f'{option} for the next {days} days in {location}')

try:
    if location:
        filter_data = get_data(location, days)

        if option == 'Graph':
            temperature = [(dict['main']['temp']* (9/5) + 32) / 10 for dict in filter_data]
            dates = [dict['dt_txt'] for dict in filter_data]
            figure = px.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature(f)'})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "sky_images/clear.png", "Clouds": "sky_images/cloud.png",
                      "Rain": "sky_images/rain.png", "Snow": "sky_images/snow.png"}
            sky_condition = [dict['weather'][0]['main'] for dict in filter_data]
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width=115)

except KeyError:
    st.write("Please Enter a Valid Zip Code")