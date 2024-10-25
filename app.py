import streamlit as st
from query_data import query_rag
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path='env/.env')

# Get OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Title of the app
st.title("Game Rules Chatbot")

# Input field for user query
query_text = st.text_input("Ask a question about Monopoly, Uno, or Yahtzee rules:")

# Select embedding type
embedding_type = st.selectbox("Select embedding type:", ["openai", "ollama"], index=0)

# Button to submit the query
if st.button("Get Answer"):
    if query_text:
        # Call the query_rag function and get the response
        response = query_rag(query_text, embedding_type)
        st.write("Response:", response)
    else:
        st.write("Please enter a question.")
