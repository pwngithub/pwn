import streamlit as st

st.set_page_config(page_title="App Launcher", layout="centered")

st.title("📊 PWN Dashboard")

# Map app names to Streamlit-hosted URLs
app_urls = {
    "Select an App": None,
    "Survey": "https://pwngithub-pwnsurvey.streamlit.app",
    "Tally": "https://pwngithub-tally.streamlit.app",
    "Prep": "https://pwngithub-pwnprep.streamlit.app"
}

selected_app = st.selectbox("Choose an app to open:", list(app_urls.keys()))

if selected_app != "Select an App":
    url = app_urls[selected_app]
    st.markdown(f"Redirecting to **{selected_app}**...")
    st.markdown(
        f"""
        <meta http-equiv="refresh" content="0;URL='{url}'" />
        """,
        unsafe_allow_html=True
    )
