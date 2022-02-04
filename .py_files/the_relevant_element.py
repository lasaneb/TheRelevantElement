import streamlit as st
import pandas as pd
from helium import *
import shutil
import time
from selenium import webdriver
from newsapi import NewsApiClient
from multiapp import MultiApp

from apps import home, data, top_headlines #wombo_art_using_helium_driver # import your app modules here

relevant_element = MultiApp()

st.markdown("Some Text Here")

# Add all your applications here as tabs

relevant_element.add_app("Home", home.app)
relevant_element.add_app("data", data.app)
relevant_element.add_app("headlines", top_headlines.app)
# relevant_element.add_app("Wombo Art", wombo_art_using_helium_driver.app)


# The main app
relevant_element.run()