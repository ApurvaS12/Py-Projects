import streamlit as st

st.title("Contact Me")



with st.form(key="contact"):
    user_email = st.text_input("**Your Email Address**")
    message = st.text_area("**Your message**")
    button =  st.form_submit_button("Submit")

    
