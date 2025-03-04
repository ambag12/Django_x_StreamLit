import streamlit as st
import requests
import datetime

appointment_list=[]
st.header("Next Page - Protected API")
with st.form("patient_form", clear_on_submit=True):
    st.header("Patient info")
    email = st.text_input("Mail:")
    number = st.text_input("no.:")
    appointments = st.text_input("Appointment")
    created_at = st.text_input("Created at",datetime.datetime.now())
    updated_at = st.text_input("Updated at",datetime.datetime.now())
    login_submit = st.form_submit_button("Submit")
    if "token" in st.session_state and "username" in st.session_state and "password" in st.session_state:
        token = st.session_state.token
        username=st.session_state.username
        password=st.session_state.password
        url = "http://127.0.0.1:8000/api/userlist/"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        body={
    "username": username,
    "password": password,
    "email": email,
    "phone_number": number,
    "appointments": appointment_list.append(appointments),
    "created_at": created_at,
    "updated_at": updated_at
    }
        response = requests.post(url, headers=headers, json=body)

        if response.status_code == 200:
            st.success("Data fetched successfully!")
            st.json(response.json())
        else:
            st.error(f"Failed to fetch data: {response.status_code} - {response.text}")

    else:
        st.warning("You must log in first to access this page.")
