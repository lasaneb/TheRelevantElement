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
        newsapi = NewsApiClient(api_key="6979450998b44ae483661232ae2c1fd3")
        relevant_articles = newsapi.get_everything(q=keyword,
                                        language='en', 
                                        sort_by='relevancy', 
                                        page_size=100)
        return relevant_articles




        all_relevant_articles = pd.DataFrame(columns = ["source", "author",	"title", "description",	"url","urlToImage", "publishedAt", "content", "keyword", "article_sentiment", "article_confidence"])

        keywords = ['Helping', 'Forgiveness', 'Positive']

        for word in keywords:
            relevant_articles = scan_for_articles(word)
            df = pd.DataFrame(relevant_articles['articles'])
            df["keyword"] = word
            all_relevant_articles = pd.concat([all_relevant_articles, df],ignore_index=True)

        # Clean the data in the source column
     
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