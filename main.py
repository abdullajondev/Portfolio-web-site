import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Home", )

col1, col2 = st.columns(2)

with col1:
    st.image("images/myphoto.Jpg", width=500)

with col2:
    st.title("Abdulla Norboboyev")
    content = """
    I have been learing python programming language by selfstudy.
    I bought a course in Udemy.com . 
    To learn anything by selfstudy that is the best choice because I am good at selfstudy .
     I believe in myself I can learn anything in short period by that method.
     Lorem20    
    """
    st.info(content)

content1 = """
Below you can find some of the app I have built in Python. Feel free to contact me.
"""
st.write(content1)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])