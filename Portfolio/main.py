import streamlit as st 
import pandas as pd

st.set_page_config(layout="wide")
col1 , col2 =  st.columns(2)

with col1:
    st.image("images/photo.jpg" )

with col2:
    st.title("Apurva Srivastava")
    content = """ Hi, I am Apurva. I am a LLM App Developer 
    I am a bachelor of technology in computer science, 
    after which I pursued MBA to hone my leadership skills.
    I am a dedicated professional with a strong work ethic,
    quick learner, and enthusiastic team player.
    Committed to delivering top-notch results 
    through effective communication, problem-solving, 
    and meticulous attention to detail in dynamic environments. """
    st.info(content)


st.write("Below you can find some of the apps I have built in Python.\
         Feel free to contact me!")


df = pd.read_csv("data.csv ", sep = ";")

col3, col4 =  st.columns(2)

with col3:
    for index , row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index , row in df[10:].iterrows():
        st.header(row["title"])