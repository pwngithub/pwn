import streamlit as st
import importlib

APPS = {
    "Survey": "apps.survey",
    "Prep": "apps.prep",
    "Dashboard": "apps.dashboard",
}

st.sidebar.title("🧭 App Dashboard")
selected_app = st.sidebar.radio("Choose an app", list(APPS.keys()))
app_module = importlib.import_module(APPS[selected_app])
app_module.run()
