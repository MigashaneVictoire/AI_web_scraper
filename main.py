# imports
import streamlit as st

st.title("Web Scraper AI") # add a title
url = st.text_input("Enter a site URL") # text input box

if st.button("Fetch"):
    st.write("scraping the site ... (DO NOT refresh site)") # writen after button pressed


