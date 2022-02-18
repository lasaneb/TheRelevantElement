
import os
import pandas as pd
import time
import streamlit as st
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
news_api_key = os.getenv("news_api_key")


def app():
    @st.cache(allow_output_mutation=True)
    def top_headlines():
        news_api_key = os.getenv("news_api_key")
        newsapi = NewsApiClient(api_key="6979450998b44ae483661232ae2c1fd3")
        top_articles = newsapi.get_top_headlines(country="us", language='en')

        return top_articles

    top_headlines_df = pd.DataFrame.from_dict(top_headlines()['articles'])
    top_headlines_df["source"] = top_headlines_df["source"].apply(lambda x: x['name'])
    summary_top_headlines_df = top_headlines_df.loc[:, ['source', 'title', 'description']]




##############################################################################################################
# Streamlit Integration #
##############################################################################################################

    st.title('Headlines')

    if st.button('Click here to see all headlines!'):
        with st.spinner('Getting Headlines...'):
            time.sleep(4)    
            st.write('Here are the Headlines!')
            st.write(summary_top_headlines_df)

    options = st.multiselect(
            'Choose your Headlines',
        [summary_top_headlines_df['title'][i] for i in range(len(summary_top_headlines_df))],
        [])

    st.write('You selected:', options)

    if st.button('Click here to open in browser!'):
        with st.spinner('Opening Headlines...'):
            time.sleep(4)    

