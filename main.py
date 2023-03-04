import streamlit as st

st.title('Weather Forecast')
location = st.text_input("Location: ")
days = st.slider('Forecast by Days', min_value=1, max_value=7,
                 help="Select the number of forecast days")

option = st.selectbox("Select Data to View", ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} days in {location}')