import streamlit as st
import requests
import json

# Streamlit UI
base_url="http://127.0.0.1:8000/"
with st.form("login_form", clear_on_submit=True):
        st.header("User Login")
        login_username = st.text_input("Enter Username", key="login_username")
        login_password = st.text_input("Enter Password", type="password", key="login_password")
        login_submit = st.form_submit_button("Login")
        
        if login_submit:
            url = base_url + "api/login"
            payload = {
                "user": login_username,
                "password": login_password
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                st.session_state.token = data.get("token")
                st.session_state.re_token = data.get("token_refresh")
                st.success("Login successful!")
                st.write("Access token:", st.session_state.token)
                st.write("Refresh token:", st.session_state.re_token)
                st.session_state.username=login_username
                st.session_state.password=login_password
            else:
                st.error(f"Login failed: {response.text}")