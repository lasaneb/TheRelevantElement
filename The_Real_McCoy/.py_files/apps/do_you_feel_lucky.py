# Initial imports

import streamlit as st
from streamlit_player import st_player
from helium import *
import time


# Embed a youtube video

helium.start_chrome('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley', headless=False)
#time.sleep(5)
#helium.kill_browser()