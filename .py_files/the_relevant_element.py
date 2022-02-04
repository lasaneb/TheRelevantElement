import streamlit as st
import pandas as pd

from multiapp import MultiApp

from apps import home# import your app modules here

relevant_element = MultiApp()

st.markdown("Some Text Here")

# Add all your applications here as tabs

relevant_element.add_app("Home", home.app)
# relevant_element.add_app("Data", data.app)


# The main app
relevant_element.run()