import os
import pandas as pd
import time
import streamlit as st
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from selenium import webdriver
import selenium
from pathlib import Path


##############################################################################################################
# Streamlit Integration #
##############################################################################################################
# # Initialize columns
#     col1, col2 = st.columns(2)

@st.cache
def get_data():
    csv = Path("all_relevant_articles.csv")
    summary_top_headlines_df = pd.read_csv(csv)
    summary_top_headlines_df_title_and_url = summary_top_headlines_df[['title', 'url']]
    return summary_top_headlines_df_title_and_url
    
csv = Path("all_relevant_articles.csv")

summary_top_headlines_df = pd.read_csv(csv)
summary_top_headlines_df_title_and_url = summary_top_headlines_df[['title', 'url']]

st.title('Articles')

if st.button('Click here to see all headlines!'):
        with st.spinner('Getting Articles...'):
            time.sleep(4)    
            st.write('Here are the Articles!')
            st.write(summary_top_headlines_df)



chosen_headlines = st.multiselect(
            'Choose your Headlines',
    [summary_top_headlines_df_title_and_url['title'][i] for i in range(len(summary_top_headlines_df_title_and_url))],
    [])

st.write('You selected:', chosen_headlines)

if st.button('Click here to open in browser!'):
    with st.spinner('Opening Headlines...'):
        # Create webdriver
        driver = webdriver.Chrome()
        # Assign URL
        #first_url = chosen_headlines[0]
        first_url = summary_top_headlines_df_title_and_url.loc[summary_top_headlines_df_title_and_url['title'] == chosen_headlines[0], 'url']
  
            # New Url
        #new_urls = [chosen_headlines[1:]]

        
        # Opening first url
        driver.get(first_url)
  
        #Open a new window
        # driver.execute_script("window.open('');")
  
        # #Switch to the new window and open new URL
        # driver.switch_to.window(driver.window_handles[1])
        # driver.get(new_urls[0])

        # driver.execute_script("window.open('');")
        # driver.switch_to.window(driver.window_handles[2])
        # driver.get(new_urls[1])
        #     # time.sleep(4)

  

