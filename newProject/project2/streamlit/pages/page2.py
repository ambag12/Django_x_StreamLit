import streamlit as st
import requests
import json

# Streamlit UI
base_url="http://127.0.0.1:8000/"
with st.form("signup_form", clear_on_submit=True):
    st.header("User Signup")
    signup_username = st.text_input("Enter Username", key="signup_username")
    signup_password = st.text_input("Enter Password", type="password", key="signup_password")
    signup_submit = st.form_submit_button("Sign up")
    
    if signup_submit:
        url = base_url + "api/signup"
        payload = {
            "user": signup_username,
            "password": signup_password
        }
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            st.success("Signup successful!")
            st.write(response.json())
        else:
            st.error(f"Signup failed: {response.text}")
