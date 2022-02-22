# Initial imports

import streamlit as st
from streamlit_player import st_player
from helium import *
import time
from selenium import webdriver

driver = webdriver.Chrome()

# Embed a youtube video

helium.start_chrome('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley', headless=False)
helium.click("Play")


if st.button("MAKE IT STOP!!!"):
    helium.kill_browser()