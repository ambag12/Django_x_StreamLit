import streamlit as st
import requests


st.header("Next Page - Protected API")

# Check if the token exists
if "token" in st.session_state:
    token = st.session_state.token

    url = "http://127.0.0.1:8000/api/doctors/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    body={
  "id": 5,
  "specialization": "Cardiology",
  "username": {
    "id": 11,
    "username": "dr_smith",
    "email": "smith@example.com",
    "phone_number": "0987654321",
    "created_at": "2024-02-20T09:00:00Z",
    "updated_at": "2024-02-21T09:00:00Z"
  },
  "clinic": {
    "id": 3,
    "name": "City Clinic",
    "address": "123 Main Street",
    "created_at": "2024-01-10T08:00:00Z",
    "updated_at": "2024-01-15T08:00:00Z"
  },
  "created_at": "2024-02-20T09:00:00Z",
  "updated_at": "2024-02-21T09:00:00Z"
}

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        st.success("Data fetched successfully!")
        st.json(response.json())
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")

else:
    st.warning("You must log in first to access this page.")
