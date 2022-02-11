import streamlit as st
import pandas as pd
from helium import *
import shutil
import time
from selenium import webdriver
# from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from multiapp import MultiApp

from apps import home, art_gallery

relevant_element = MultiApp()

st.markdown("Welcome to an Art Gallery of Relevance!")

# Add all your applications here as tabs

relevant_element.add_app("Home", home.app)
relevant_element.add_app("Art Gallery", art_gallery.app)


# The main app
relevant_element.run()