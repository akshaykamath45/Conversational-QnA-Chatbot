from dotenv import load_dotenv
load_dotenv() # loads all the environment variables

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))