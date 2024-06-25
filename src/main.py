import os

import streamlit as st

from doc_chat_utility import get_answer

working_dir = os.path.dirname(os.path.abspath(__file__)) # Finds absolute path to files for streamlit

st.set_page_config(
    page_title="RAG APP",
    page_icon="📄",
    layout="centered"
)

st.title("PDF RAG APPLICATION")

uploaded_file = st.file_uploader(label="Upload your file", type=["pdf"])

user_query = st.text_input("Ask your question")

# if st.button("Run"):
#     bytes_data = uploaded_file.read()
#     file_name = uploaded_file.name
#     # save the uploaded file to the working directory
#     file_path = os.path.join(working_dir, file_name)
#     with open(file_path, "wb") as f:
#         f.write(bytes_data)
#     answer = get_answer(file_name, user_query)
#
#     st.success(answer)

if st.button("Run"):
    if uploaded_file is not None and user_query.strip() != "":
        bytes_data = uploaded_file.read()
        file_name = uploaded_file.name
        # save the uploaded file to the working directory
        file_path = os.path.join(working_dir, file_name)
        with open(file_path, "wb") as f:
            f.write(bytes_data)
        answer = get_answer(file_name, user_query)

        st.success(answer)
    else:
        st.error("Please upload a file and enter a query.")
