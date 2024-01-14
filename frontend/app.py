import streamlit as st
import requests
from requests.exceptions import HTTPError

st.title("RAG App")

# Display "Hello, world!" on the app
st.write("Test App!")

# Create a button with the label "Test backend"
button = st.button("Test backend")

# If the button is clicked, send a GET request to localhost:80/ and display the response
if button:
    try:
        response = requests.get("http://backend:8000/s")
        response = response.text
    except HTTPError as err:
        response = f"Not working! (Code {err.response.status_code})"
    st.write(response)


# st.write("Upload a PDF document and ask a question about it. The app will use a large language model to generate an answer based on the document.")

# pdf = st.file_uploader("Choose a PDF file", type="pdf")
# question = st.text_input("Enter your question")

# if st.button("Get answer"):
#     # TODO: implement the logic to send the PDF and the question to the backend API and display the answer
#     # Hint: use requests.post to make a POST request to the API endpoint
#     answer = "This is a dummy answer"
#     st.write(answer)
