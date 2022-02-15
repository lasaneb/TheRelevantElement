from random import randint
import streamlit as st
import time
import os
import pandas as pd
import time
import streamlit as st
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient


def app():

    st.title('Home')

    st.write('With this app we will do some cool stuff.')

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
                time.sleep(20)
                index += 1
            # st.write(top_headlines_df)

# Image Carosel

def main():

    images = ["https://ipfs.io/ipfs/QmeTuPqzFWosFkCycvoN29jkfbMXDGWMMLMBMnStYXMW5W?filename=Dream.jpg",
              "https://ipfs.io/ipfs/QmNZAoco2BLbTnpqyBMmJ2CkH3ncoMbJofKWfRC9jX9UCy?filename=everything_is_awesome.jpg",
              "https://ipfs.io/ipfs/QmR1UCsrPNAUPKPtB133VtUMkyhTFLaqepmLnqkfahrHWU?filename=Family_and_Love.jpg",
              "https://ipfs.io/ipfs/QmV5nZAeLJmmWknrfQEPxNba8JUqA5dpd8ZWdJtSanXkVz?filename=The_hot_sauce_is_mine.jpg"
              "https://ipfs.io/ipfs/QmVvdRRgUXDHuRR5Bd9FiYXFptsThqdouJdDxXGB2pA4Uc?filename=thief_in_the_night.jpg"
              ]

    captions = ["Dream", "Everything is Awesome", "Family and Love", "The hot sauce is mine", "Thief in the night"]




   

    



    

    