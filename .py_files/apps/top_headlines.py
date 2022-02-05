# Streamlit Interface

import streamlit as st


from dataclasses import dataclass
from typing import Any, List
import os
# from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from datetime import date, timedelta
import pandas as pd
import pdfkit
import flair
#news_api_key = os.getenv("news_api_key")

# Define a function to retrieve top headlines for Country USA

def top_headlines():
    newsapi = NewsApiClient(api_key=st.secrets["news_api_key"])
    top_articles = newsapi.get_top_headlines(country="us", language='en')

    return top_articles

st.markdown("# Top Headlines")
st.button("Click to get headlines")
# if st.button("Click to get headlines"):
#     top_articles = top_headlines()
#     st.write(top_articles)

#top_headlines = pd.DataFrame(app()['articles']) 

#st.write(top_headlines)