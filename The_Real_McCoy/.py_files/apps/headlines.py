
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




##############################################################################################################
# Streamlit Integration #
##############################################################################################################

    st.title('Headlines')

   

    if st.button('Click here to get headlines!'):
        with st.spinner('Getting Headlines...'):
            time.sleep(4)    
            st.write('Here are the Headlines!')
            # textPlaceholder = st.empty()
            index = 0
            textPlaceholder = st.empty()
            for row in top_headlines_df['title']:
                textPlaceholder.text(top_headlines_df['title'][index])
                index += 1
            # st.write(top_headlines_df)    

