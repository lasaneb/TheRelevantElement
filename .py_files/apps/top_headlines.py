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

st.markdown("# Top Headlines")
st.button("Click to get headlines")


    # Get top headlines for Country USA
@st.cache
def app():
    newsapi = NewsApiClient(api_key=st.secrets["news_api_key"])
    top_articles = newsapi.get_top_headlines(country="us", language='en')

    return top_articles

top_headlines = pd.DataFrame(app()['articles']) 

st.write(top_headlines)