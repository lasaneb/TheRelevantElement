import os
import pandas as pd
import time
import streamlit as st
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
# from selenium import webdriver
# from pathlib import Path
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# news_api_key = os.getenv("news_api_key")



@st.cache(allow_output_mutation=True)
def top_headlines():
        #news_api_key = os.getenv("news_api_key")
        newsapi = NewsApiClient(api_key= st.secrets['news_api_key'])
        top_articles = newsapi.get_top_headlines(country="us", language='en')

        return top_articles

top_headlines_df = pd.DataFrame.from_dict(top_headlines()['articles'])
top_headlines_df["source"] = top_headlines_df["source"].apply(lambda x: x['name'])
summary_top_headlines_df_title_and_url = top_headlines_df[['title', 'url']]
summary_top_headlines_df_title_and_url.set_index('title', inplace=True, drop=False)
top_headlines_df = top_headlines_df[['source', 'title']]
    

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
            st.dataframe(top_headlines_df)

chosen_headlines = st.multiselect(
            'Choose your Headlines',
            summary_top_headlines_df_title_and_url['title'],
    [])

st.write('You selected:', chosen_headlines)

# if st.button('Click here to open in browser!'):
#         with st.spinner('Opening Headlines...'):
#         # Create webdriver
#         #driver = webdriver.Chrome()
        
#             options = Options()
#             options.page_load_strategy = 'eager'
#             options.add_experimental_option("detach", True)
#             driver = webdriver.Chrome(options=options)


        # Assign URL
        #first_url = chosen_headlines[0]
        # first_url = summary_top_headlines_df_title_and_url.loc[chosen_headlines[0]]['url']
        # driver.get(first_url)
        # index = 0
        # for item in chosen_headlines:
        #     url = summary_top_headlines_df_title_and_url.loc[item]['url']
        #     # Open new browser and go to first URL
        #     driver.execute_script("window.open('');")
        #     #Open a new tab
        #     driver.switch_to.window(driver.window_handles[index])
        #     driver.get(url)
        #     index += 1
            
  
            # #Open a new window
            # driver.execute_script("window.open('');")
  
            # #Switch to the new window and open new URL
            # driver.switch_to.window(driver.window_handles[1])
            # driver.get(new_urls[0])

            # driver.execute_script("window.open('');")
            # driver.switch_to.window(driver.window_handles[2])
            # driver.get(new_urls[1])
            # # time.sleep(4)

