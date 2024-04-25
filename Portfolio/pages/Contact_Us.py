import streamlit as st
from send_email import send_email 
import pandas as pd

options_df = pd.read_csv("topics.csv")

options = options_df["topic"].tolist()

st.title("Contact Me")



with st.form(key="contact"):
    user_email = st.text_input("**Your Email Address**")
    option = st.selectbox("**Select an option**" , options)
    raw_message = st.text_area("**Your message**")
    message =  f"""\
Subject: New email from {user_email}

From: {user_email}
Topic : {option}
{raw_message}
"""
    button =  st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Message sent successfully!")
