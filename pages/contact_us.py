import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email forms"):
    user_email = st.text_input("Your email adress")
    row_message = st.text_area("your message")
    message = f"""\
Subject: New Email form {user_email}

From {user_email}
{row_message}

"""
    button = st.form_submit_button()
    print(button)
    if button:
        send_email(message)
        st.info("Your email was sent")
