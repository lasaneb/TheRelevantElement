

from PIL import Image
import streamlit as st
from itertools import cycle
import time
from multiapp import MultiApp
from apps import art_gallery, wombo_art_generator

relevant_element = MultiApp()

def app():
    st.title('Art Gallery')

    st.write('Enjoy this art gallery!')

relevant_element.add_app("Home", art_gallery.app)
relevant_element.add_app("Generate Art with Wombo", wombo_art_generator.app)


# The main app
relevant_element.run()
    








