import textwrap

import streamlit as st
from functions.youtube_assistant import *

st.title("YouTube Assistant")
st.caption("Only limited to English as of now :)")

with st.form(key='my_form'):
    youtube_url = st.text_area(
            label="Input Youtube Url:",
            max_chars=50
            )
    query = st.text_area(
            label="What do you want to know about the video:",
            max_chars=500,
            key="query"
            )

    submit_button = st.form_submit_button(label='Submit')

if submit_button:

    db = create_vector_db_from_youtube_url(youtube_url)
    response, docs = get_response_from_query(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=85))