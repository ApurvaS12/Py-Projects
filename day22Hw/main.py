import streamlit as st 
import pandas as pd

st.set_page_config(layout="wide")



st.title("The Best Company")

content = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Curabitur sollicitudin hendrerit euismod. Vestibulum ante 
            ipsum primis in faucibus orci luctus et ultrices posuere 
            cubilia curae; Fusce elementum velit ut ligula semper 
            auctor. Phasellus sit amet volutpat lectus, eu molestie
            enim. Donec massa massa, faucibus ac purus sit amet, 
            dignissim elementum nisi. Proin imperdiet dui maximus,
            congue magna vel, accumsan nisi. Ut vitae nisi sapien. 
            Quisque neque ipsum, pulvinar sed posuere ut, blandit nec sem. 
            Nulla at pharetra justo, ac rutrum ante. Sed aliquam dolor at ligula 
            consequat mattis. Phasellus ut orci sed sapien finibus varius at sit amet augue. 
            Sed ut tincidunt leo. Ut ac ex porttitor, 
            scelerisque ligula quis, pharetra risus."""

st.write(content)

#st.write("**BOLD TExt**")

st.header("MEET OUR TEAM")

col1 , emp1, col2, emp2, col3 = st.columns([1.5,0.5, 1.5,  0.5,1.5])

df = pd.read_csv("data.csv")




with col1:
    for index, row in df[:4].iterrows():
        name = f"{row['first name']}  {row['last name']}"
        st.subheader(name.title())
        job_title = row["role"]
        st.write(f"**{job_title}**")
        st.image("images/" + row["image"])
        st.write("            ")


with col2:
    for index, row in df[4:8].iterrows():
        name = f"{row['first name']}  {row['last name']}"
        st.subheader(name.title())
        job_title = row["role"]
        st.write(f"**{job_title}**")
        st.image("images/" + row["image"])
        st.write("            ")

with col3:
    for index, row in df[8:12].iterrows():
       name = f"{row['first name']}  {row['last name']}"
       st.subheader(name.title())
       job_title = row["role"]
       st.write(f"**{job_title}**")
       st.image("images/" + row["image"])
       st.write("              ")
