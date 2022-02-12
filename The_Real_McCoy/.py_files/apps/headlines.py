
import os
import pandas as pd
import time
import streamlit as st
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
news_api_key = os.getenv("news_api_key")

def app():

    def top_headlines():
        news_api_key = os.getenv("news_api_key")
        newsapi = NewsApiClient(api_key="6979450998b44ae483661232ae2c1fd3")
        top_articles = newsapi.get_top_headlines(country="us", language='en')

        return top_articles

    top_headlines_df = pd.DataFrame.from_dict(top_headlines()['articles'])
    top_headlines_df["source"] = top_headlines_df["source"].apply(lambda x: x['name'])

    def make_clickable(url):
        return f'<a target="_blank" href="{url}">{url}</a>'

    top_headlines_df.style.format({'url': make_clickable})


##############################################################################################################
# Streamlit Integration #
##############################################################################################################

    st.title('Headlines')


    st.write('This is where we will get headlines.')

    if st.button('Click here to get headlines'):
        st.spinner('Getting Headlines...')
        time.sleep(4)    
        st.write('Here are the headlines:')
        st.write(top_headlines_df)    

