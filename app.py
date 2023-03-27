import streamlit as st

st.set_page_config(
    page_title="Saved Blog Manager",
    page_icon="📖",
    initial_sidebar_state="expanded",
    menu_items={
        "Report a bug": "https://github.com/Samir84753/Streamlit-Webapp/issues",
        "About": "This is a web application made with Streamlit.",
    },
)
st.title("APP")
st.markdown(
    """
        **Github Repo:** https://github.com/Samir84753/Streamlit-Webapp
    """
)
