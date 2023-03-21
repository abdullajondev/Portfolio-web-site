import streamlit as st

st.header("Contact Me")

with st.form(key="email forms"):
    user_email = st.text_input("Your email adress")
    message = st.text_area("your message")
    button = st.form_submit_button()