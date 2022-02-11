import streamlit as st
import pandas as pd
import time
from multiapp import MultiApp

from apps import home, art_gallery

relevant_element = MultiApp()

st.markdown("Welcome to an Art Gallery of Relevance!")

# Add all your applications here as tabs

relevant_element.add_app("Home", home.app)
relevant_element.add_app("Art Gallery", art_gallery.app)


# The main app
relevant_element.run()