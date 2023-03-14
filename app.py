import streamlit as st

st.set_page_config(
    page_title="Saved Blog Manager",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "https://github.com/Samir84753/Streamlit-Webapp",
        'About': "# This is a header. This is an *extremely* cool app!"
    })
st.title("APP")