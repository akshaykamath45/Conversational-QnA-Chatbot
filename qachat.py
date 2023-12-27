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

# intializing session state for chat history if it doesn't exists
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


input=st.text_input("Input:",key="input") # user input or question
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is ") 
    
    # process does not have to wait for the entire content to come from LLM
    # whatever response it is sending , we will display it in the frontend screen
    # stream=True -> we get access of all the streaming data
    
    complete_response=""
    for chunk in response:
        complete_response+=chunk.text
    st.write(complete_response) # this will display the immideate response
    st.session_state['chat_history'].append(("Bot",complete_response)) # this will append to chat history


# displaying chat history 
st.subheader("The Chat History is ")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}", unsafe_allow_html=True)
