import streamlit as st
import os
from dotenv import load_dotenv
from query_data import query_rag

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is set
if openai_api_key is None:
    st.error("OpenAI API key not found. Please set it in the .env file.")
    st.stop()  # Stop the app if the API key is not found

# Title of the app
st.title("Game Rules Chatbot")

# Input field for user query
query_text = st.text_input("Ask a question about Monopoly, Uno, or Yahtzee rules:")

# Select embedding type
embedding_type = st.selectbox("Select embedding type:", ["openai", "ollama"], index=0)

# Button to submit the query
if st.button("Get Answer"):
    if query_text:  # Check if the user has entered a question
        try:
            # Call the query_rag function and get the response
            response = query_rag(query_text, embedding_type)
            st.write("Response:", response)
        except Exception as e:  # Catch any errors during query processing
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question.")  # Warning if no question is entered
