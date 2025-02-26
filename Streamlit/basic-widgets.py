import datetime

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


name = st.text_input("Enter your name", value='')
st.write("Name: ", name)

text = st.text_area("Feedback")
st.write("Feedback: ", text)

number = st.number_input("Umur")
st.write("Umur: ", int(number), ' tahun')


date = st.date_input("Tanggal lahir", min_value=datetime.date(1990,1,1))
st.write("Tanggal lahir: ", date)


uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

#
# picture = st.camera_input("Take a picture")
# if picture is not None:
#     st.image(picture)

if st.button("Say Hello"):
    st.write("Hello There")


agree = st.checkbox("I Agree")

if agree:
    st.write("Welcome to MyApp")

genre = st.radio(
    label="What's your favorite movie genre?",
    options=("Comedy", "Drama", "Documentry"),
    horizontal=False
)

genreSelect = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

genreMulti = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

values = st.slider(
    label="Select a range of values",
    min_value=0,max_value=100, value=(0, 100)
)
st.write("Values: ", values)