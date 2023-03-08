import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast')
location = st.text_input("Location: ")
days = st.slider('Forecast by Days', min_value=1, max_value=5,
                 help="Select the number of forecast days")

option = st.selectbox("Select Data to View", ('Graph', 'Sky'))

st.subheader(f'{option} for the next {days} days in {location}')

if location:
    filter_data = get_data(location, days)

    if option == 'Graph':
        temperature = [dict['main']['temp'] for dict in filter_data]
        dates = [dict['dt_txt'] for dict in filter_data]
        figure = px.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature'})
        st.plotly_chart(figure)

    if option == "Sky":
        sky_condition = [dict['weather'][0]['main'] for dict in filter_data]
        st.image()