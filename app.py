from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image

load_dotenv()

logo = Image.open('icon.jfif')
st.set_page_config(page_title = 'ChatBot', page_icon = logo)

#st.title('Simple ChatBot using LangChain')
st.markdown("<h1 style='text-align:center; color:black;'>ChatBot using LangChain</h1>", unsafe_allow_html = True)

with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

input = st.text_input('Please enter your input here:')

response_button = st.button('Get Response', type = 'primary')


if response_button:
    llm = OpenAI(temperature = 0.6, openai_api_key = os.getenv('OPENAI_API_KEY'))
    #llm = OpenAI(temperature = 0.6, openai_api_key = 'OPEN')
    response = llm(input)
    st.subheader('The respone is')
    st.write(response)