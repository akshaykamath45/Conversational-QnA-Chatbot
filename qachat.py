from dotenv import load_dotenv
load_dotenv() # loads all the environment variables

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response


# initializing streamlit app
st.set_page_config(page_title="Conversational QnA")
st.header("Conversational QnA Chatbot")
st.subheader("Gemini LLM Application")