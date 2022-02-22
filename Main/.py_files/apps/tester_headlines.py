import os
import pandas as pd
import time
import streamlit as st
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.options import Options


##############################################################################################################
# Streamlit Integration #
##############################################################################################################
# # Initialize columns
#     col1, col2 = st.columns(2)
csv = Path("all_relevant_articles.csv")

summary_top_headlines_df = pd.read_csv(csv)
summary_top_headlines_df_title_and_url = summary_top_headlines_df[['title', 'url']]
summary_top_headlines_df = summary_top_headlines_df[['title', 'url']]
#st.write(summary_top_headlines_df_title_and_url.head())
summary_top_headlines_df_title_and_url.set_index('title', inplace=True, drop=False)
st.title('Headlines')

if st.button('Click here to see all headlines!'):
        with st.spinner('Getting Headlines...'):
            time.sleep(4)    
            st.write('Here are the Headlines!')
            st.write(summary_top_headlines_df)



chosen_headlines = st.multiselect(
            'Choose your Headlines',
            summary_top_headlines_df_title_and_url['title'],
    #[summary_top_headlines_df_title_and_url['title'][i] for i in range(len(summary_top_headlines_df_title_and_url))],
    [])

st.write('You selected:', chosen_headlines)

if st.button('Click here to open in browser!'):
    with st.spinner('Opening Headlines...'):
        # Create webdriver
        #driver = webdriver.Chrome()
        
        options = Options()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)


        # Assign URL
        #first_url = chosen_headlines[0]
        # first_url = summary_top_headlines_df_title_and_url.loc[chosen_headlines[0]]['url']
        # driver.get(first_url)
        index = 0
        for item in chosen_headlines:
            url = summary_top_headlines_df_title_and_url.loc[item]['url']
            # Open new browser and go to first URL
            driver.execute_script("window.open('');")
            #Open a new tab
            driver.switch_to.window(driver.window_handles[index])
            driver.get(url)
            index += 1
            
            #driver.switch_to.window(driver.window_handle)


  
        #Open a new window
        # driver.execute_script("window.open('');")
  
        # #Switch to the new window and open new URL
        # driver.switch_to.window(driver.window_handles[1])
        # driver.get(new_urls[0])

        # driver.execute_script("window.open('');")
        # driver.switch_to.window(driver.window_handles[2])
        # driver.get(new_urls[1])
        #     # time.sleep(4)

  

