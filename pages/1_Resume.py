import streamlit as st

# load html and pdf file.
with open("assets/Samir_resume.html", "r") as f:
    html_string = f.read()
pdf_path = "assets/Samir_resume.pdf"
with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()

# html display
st.components.v1.html(html_string, width=950, height=1210)

# download button for resume on sidebar.
st.sidebar.download_button(
    "Download Resume",
    data=pdf_bytes,
    file_name="Samir_resume.pdf",
    mime="application/pdf",
)
