import streamlit as st

st.set_page_config(page_title="App Launcher", layout="centered")

st.title("📊 PWN Dashboard")

# App selection map with corrected URLs
app_urls = {
    "Survey": "https://pwnsurvey.streamlit.app",
    "Tally": "https://tally.streamlit.app",
    "Prep": "https://pwnprep.streamlit.app"
}

selected_app = st.selectbox("Choose an app to open:", ["Select an App"] + list(app_urls.keys()))

if selected_app != "Select an App":
    url = app_urls[selected_app]
    st.success(f"Click below to open {selected_app}")
    st.markdown(
        f'<a href="{url}" target="_blank"><button style="padding:10px 20px;">Open {selected_app}</button></a>',
        unsafe_allow_html=True
    )
