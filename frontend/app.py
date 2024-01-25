"""
RAG-QA frontend logic.
"""

import base64
import requests
import streamlit as st

st.title("💬 PDF QA")

# Create a file uploader in the sidebar
st.sidebar.title("Upload a PDF file")
uploaded_file = st.sidebar.file_uploader(
    label="Choose a file", type="pdf", accept_multiple_files=False
)

# Create a chat interface
message = st.chat_message("assistant")
message.write("Ask a question to your page.")


# Once file and question received
prompt = st.chat_input("Ask something")
if prompt and uploaded_file is not None:
    # Update user with messages
    message = st.chat_message("user")
    message.write(prompt)
    message = st.chat_message("assistant")
    message.write("Thinking...")

    # Encode the PDF file as base64 string
    encoded_pdf = base64.b64encode(uploaded_file.read()).decode("ascii")

    json_payload = {"question": prompt, "pdf": encoded_pdf}

    # Send request and display answer to user
    response = requests.post("http://backend:8000/ask", json=json_payload, timeout=120)
    message.write(response.json())
