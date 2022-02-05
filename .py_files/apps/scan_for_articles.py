# Initial Imports

import streamlit as st
import os
from newsapi import NewsApiClient
from datetime import date, timedelta
import pandas as pd
from fpdf import FPDF
#news_api_key = os.getenv("news_api_key")
import flair
from flair.data import Sentence
import requests

search_term = ["Generosity"]

def scan_for_articles():
    newsapi = NewsApiClient(api_key=st.secrets["news_api_key"])
    top_articles = newsapi.get_everything(q=search_term,

    return top_articles

top_headlines = pd.DataFrame(get_top_headlines()['articles']) 