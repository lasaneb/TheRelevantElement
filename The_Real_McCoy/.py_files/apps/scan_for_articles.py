# Initial Imports

import streamlit as st
import os
from newsapi import NewsApiClient
from datetime import date, timedelta
import pandas as pd
from fpdf import FPDF
news_api_key = os.getenv("news_api_key")
import flair
from flair.data import Sentence
import requests
import helium

def app():
    st.title('Scan for Relevant Articles')


    st.write('Scan for articles that will contain useable content.')

def scan_for_articles(keyword):
    newsapi = NewsApiClient(api_key=news_api_key)
    relevant_articles = newsapi.get_everything(q=keyword,
                                        language='en', 
                                        sort_by='relevancy', 
                                        page_size=100)
    return relevant_articles

# with st.form('keywords'):
#     keywords = st.text_input('Enter up to 3 keywords separated by commas')
#     keywords = keywords.split(',')
#     if len(keywords) > 3:
#         st.error('Uh Oh! You entered too many keywords!')
#         st.image("C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//Troll.jpg")
#         if st.button("Click here to bo back"):
#             helium.start_chrome("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
        
#     else:
#         submitted = st.form_submit_button('Submit')
#         if submitted:
#             st.write("Submitted!")


keywords = ['Helping', 'Forgiveness']
       
all_relevant_articles = pd.DataFrame(columns = ["source", "author",	"title", "description",	"url","urlToImage", "publishedAt", "content", "keyword","article_sentiment", "article_confidence"])

# keywords = ['Helping', 'Forgiveness']

for word in keywords:
    relevant_articles = scan_for_articles(word)
    df = pd.DataFrame(relevant_articles['articles'])
    df["keyword"] = word
    all_relevant_articles = pd.concat([all_relevant_articles, df],ignore_index=True)

# Clean the data in the source column
#     
all_relevant_articles["source"] = all_relevant_articles["source"].apply(lambda x: x['name'])


article_sentiment_model = flair.models.TextClassifier.load('en-sentiment')

# Initialize lists

article_sentiment = []
article_confidence = []


# Run Sentiment analysis on collected news sentences


for sentence in all_relevant_articles["description"]:
        if sentence.strip() == "":
                article_confidence.append("")
                article_sentiment.append("")
                
        else:
                sample = flair.data.Sentence(sentence)
                article_sentiment_model.predict(sample)
                article_sentiment.append(sample.labels[0].value)
                article_confidence.append(sample.labels[0].score)

# Add Results to Dataframe

all_relevant_articles['sentiment'] = article_sentiment
all_relevant_articles['confidence'] = article_confidence