# import streamlit as st
# import requests
# import json

# st.title("Hospital Management System")

# # Streamlit UI
# base_url="http://127.0.0.1:8000/"
# with st.form("signup_form", clear_on_submit=True):
#     st.header("User Signup")
#     signup_username = st.text_input("Enter Username", key="signup_username")
#     signup_password = st.text_input("Enter Password", type="password", key="signup_password")
#     signup_submit = st.form_submit_button("Sign up")
    
#     if signup_submit:
#         url = base_url + "api/signup"
#         payload = {
#             "user": signup_username,
#             "password": signup_password
#         }
#         response = requests.post(url, json=payload)
#         if response.status_code == 201:
#             st.success("Signup successful!")
#             st.write(response.json())
#         else:
#             st.error(f"Signup failed: {response.text}")

# # -----------------------------------
# # Login Form
# # -----------------------------------
# if st.button('Already have an account?'):

#     with st.form("login_form", clear_on_submit=True):
#         st.header("User Login")
#         login_username = st.text_input("Enter Username", key="login_username")
#         login_password = st.text_input("Enter Password", type="password", key="login_password")
#         login_submit = st.form_submit_button("Login")
        
#         if login_submit:
#             url = base_url + "api/login"
#             payload = {
#                 "user": login_username,
#                 "password": login_password
#             }
#             response = requests.post(url, json=payload)
#             if response.status_code == 200:
#                 data = response.json()
#                 st.session_state.token = data.get("token")
#                 st.session_state.re_token = data.get("token_refresh")
#                 st.success("Login successful!")
#                 st.write("Access token:", st.session_state.token)
#                 st.write("Refresh token:", st.session_state.re_token)
#             else:
#                 st.error(f"Login failed: {response.text}")

import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
