
import os
import pandas as pd
import time
import streamlit as st
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from selenium import webdriver
import selenium
news_api_key = os.getenv("news_api_key")


def app():
    @st.cache(allow_output_mutation=True)
    def top_headlines():
        #news_api_key = os.getenv("news_api_key")
        newsapi = NewsApiClient(api_key="6979450998b44ae483661232ae2c1fd3")
        top_articles = newsapi.get_top_headlines(country="us", language='en')

        return top_articles

    top_headlines_df = pd.DataFrame.from_dict(top_headlines()['articles'])
    top_headlines_df["source"] = top_headlines_df["source"].apply(lambda x: x['name'])
    summary_top_headlines_df = top_headlines_df.loc[:, ['source', 'title', 'description', 'url']]




##############################################################################################################
# Streamlit Integration #
##############################################################################################################
# # Initialize columns
#     col1, col2 = st.columns(2)

    st.title('Headlines')

    if st.button('Click here to see all headlines!'):
        with st.spinner('Getting Headlines...'):
            time.sleep(4)    
            st.write('Here are the Headlines!')
            st.write(summary_top_headlines_df)

    chosen_headlines = st.multiselect(
            'Choose your Headlines',
        [summary_top_headlines_df['title'][i] for i in range(len(summary_top_headlines_df))],
        [])

    st.write('You selected:', chosen_headlines)

    if st.button('Click here to open in browser!'):
        with st.spinner('Opening Headlines...'):
            # Create webdriver
            driver = webdriver.Chrome()
            # Assign URL
            first_url = summary_top_headlines_df.loc[summary_top_headlines_df['title'] == chosen_headlines[0], 'url']
  
            # New Url
            new_urls = [chosen_headlines[1:]]

            while True:
                # Opening first url
                driver.get(first_url)
  
            #Open a new window
            driver.execute_script("window.open('');")
  
            #Switch to the new window and open new URL
            driver.switch_to.window(driver.window_handles[1])
            driver.get(new_urls[0])

            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[2])
            driver.get(new_urls[1])
            # time.sleep(4)

  

