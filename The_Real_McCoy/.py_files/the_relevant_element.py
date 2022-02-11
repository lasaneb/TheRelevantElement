import streamlit as st
#import pandas as pd
#from helium import *
#from selenium import webdriver
#from newsapi import NewsApiClient
#from newsapi.newsapi_client import NewsApiClient
from multiapp import MultiApp

from apps import home, headlines, scan_for_articles, speech_recognition_and_search

relevant_element = MultiApp()

st.markdown("Welcome to the Relevant Element!")

st.button("Click Here to Donate")

# Add all your applications here as tabs

relevant_element.add_app("Home", home.app)
relevant_element.add_app("Headlines", headlines.app)
relevant_element.add_app("Scan for Articles", scan_for_articles.app)
relevant_element.add_app("Speech to Search", speech_recognition_and_search.app)

# The main app
relevant_element.run()