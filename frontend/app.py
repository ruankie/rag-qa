import streamlit as st
import requests
from requests.exceptions import HTTPError

st.title("Web Page QA")

# Create a sidebar for the web page URL input
st.sidebar.header("Enter a web page URL")
url = st.sidebar.text_input(label="URL", value="https://lilianweng.github.io/posts/2023-06-23-agent/")

# Create a chat interface
message = st.chat_message("assistant")
message.write("Ask a question to your page.")

prompt = st.chat_input("Ask something")
if prompt:
    message = st.chat_message("user")
    message.write(prompt)

    message = st.chat_message("assistant")
    message.write("Thinking...")
    
    payload = {
        "question": prompt,
        "url": url 
    }
    # message.write(payload)
    response = requests.post("http://backend:8000/ask", json=payload)
    message.write(response.text)

