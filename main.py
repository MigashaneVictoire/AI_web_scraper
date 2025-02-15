# imports
import streamlit as st
from scrape import *
from parser_ml import parse_with_ollama

st.title("Web Scraper AI") # add a title
url = st.text_input("Enter a site URL") # text input box

if st.button("Fetch"):
    st.write("scraping the site ... (DO NOT refresh site)") # writen after button pressed

    result = scrape_site(url)
    body_content = body_content_extraction(result)
    cleaned_cont = clean_content(body_content)

    st.session_state.dom_content = cleaned_cont

    with st.expander("View DOM content"):
        st.text_area("DOM content", cleaned_cont, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you are trying to parse?")

    if st.button("Parse Content"):
        if  parse_description:
            st.write("Parsing the content!")

            dom_chunks = separate_dom_content(st.session_state.dom_content)
            parse_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parse_result)