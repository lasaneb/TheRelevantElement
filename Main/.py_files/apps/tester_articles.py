import os
import pandas as pd
import time
from sklearn.decomposition import non_negative_factorization
import streamlit as st
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from selenium import webdriver
import flair
from pathlib import Path
from pathlib import Path
from selenium.webdriver.chrome.options import Options
#driver = webdriver.Chrome()


##############################################################################################################
# Streamlit Integration #
##############################################################################################################
# # Initialize columns
# col1, col2,  = st.columns(2)

@st.cache
def get_data():
    csv = Path("all_relevant_articles.csv")
    summary_articles_df = pd.read_csv(csv)
    #summary_articles_df_title_and_url = summary_articles_df[['title', 'description', 'url']]
    #return summary_top_headlines_df_title_and_url
    driver = webdriver.Chrome()

csv = Path("all_relevant_articles.csv")

summary_articles_df_all = pd.read_csv(csv)

# article_sentiment_model = flair.models.TextClassifier.load('en-sentiment')

#     # Initialize lists

# article_sentiment = []
# article_confidence = []

#         # Run Sentiment analysis on collected news sentences

# for sentence in summary_articles_df["description"]:
#             # if sentence.strip() == "":
#             #     article_confidence.append("")
#             #     article_sentiment.append("")
                
# # else:
#     sample = flair.data.Sentence(sentence)
# article_sentiment_model.predict(sample)
# article_sentiment.append(sample.labels[0].value)
# article_confidence.append(sample.labels[0].score)

            # Add Results to Dataframe

# summary_articles_df['sentiment'] = article_sentiment
# summary_articles_df['confidence'] = article_confidence


st.title("Get Useable Content")
st.write("First select if you want to see articles that will tend to be positive or negative.")
st.write("Then use the slider to set the threhold; the lower the threshold, the more articles will be shown, but may include elements of the opposite sentiment.")


threshold = st.slider('Set Threshold.', 0, 100, 80)

sentiment = st.radio('Sentiment', ('POSITIVE', 'NEGATIVE'))
threshold_percentage = threshold / 100

summary_articles_df = summary_articles_df_all[summary_articles_df_all['sentiment'] == sentiment] 
summary_articles_df = summary_articles_df[summary_articles_df['confidence'] >= threshold_percentage]
summary_articles_df = summary_articles_df[['title', 'url']]
length = str(len(summary_articles_df)) 

if st.button("Generate Articles"):
    st.write("Here are the articles you selected!")
    st.write("There are " + length + " articles.")
    st.write(summary_articles_df)
    
    # positive_articles = summary_articles_df[summary_articles_df['sentiment'] == "POSITIVE"]
    # negative_articles = summary_articles_df[summary_articles_df['sentiment'] == "NEGATIVE"]
    # very_strongly = 98 / 100
    # strongly = 95 / 100
    # somewhat = 85 / 100
    # not_strongly = 70 / 100
    # neutral = 55 / 100

    
    # # These are options for the multi choice slider
    # very_strongly_positive_articles = positive_articles[positive_articles['confidence'] >= very_strongly]
    # strongly_positive_articles = positive_articles[(positive_articles['confidence'] >= somewhat) & (positive_articles['confidence'] < very_strongly)]
    # somewhat_positive_articles = positive_articles[(positive_articles['confidence'] >= not_strongly) & (positive_articles['confidence'] < somewhat)]
    # not_strongly_positive_articles = positive_articles[(positive_articles['confidence'] >= neutral) & (positive_articles['confidence'] < not_strongly)]
    # neutral_positive_articles = positive_articles[(positive_articles['confidence'] >= not_strongly) & (positive_articles['confidence'] < neutral)]
    # neutral_negative_articles = negative_articles[(negative_articles['confidence'] >= not_strongly) & (negative_articles['confidence'] < neutral)]
    # not_strongly_negative_articles = negative_articles[(negative_articles['confidence'] >= neutral) & (negative_articles['confidence'] < not_strongly)]
    # somewhat_negative_articles = negative_articles[(negative_articles['confidence'] >= somewhat) & (negative_articles['confidence'] < neutral)]
    # strongly_negative_articles = negative_articles[(negative_articles['confidence'] >= very_strongly) & (negative_articles['confidence'] < somewhat)]
    # very_strongly_negative_articles = negative_articles[negative_articles['confidence'] >= very_strongly]

    # chosen_articles = st.select_slider('Choose what kind of articles you would like to see', (very_strongly_positive_articles, strongly_positive_articles, somewhat_positive_articles, not_strongly_positive_articles, neutral_positive_articles, neutral_negative_articles, not_strongly_negative_articles, somewhat_negative_articles, strongly_negative_articles, very_strongly_negative_articles))
    # if st.button("Generate Articles"):
    #     st.write(chosen_articles)

summary_articles_df_title_and_url = summary_articles_df[['title', 'url']]
summary_top_headlines_df = summary_articles_df_all[['title', 'url']]
summary_articles_df_title_and_url.set_index('title', inplace=True, drop=False)

chosen_headlines = st.multiselect(
             'Choose your Headlines',
             summary_articles_df_title_and_url['title'],
     [])

st.write('You selected:', chosen_headlines)

if st.button('Click here to open in browser!'):
     with st.spinner('Opening Articles...'):
        #Create webdriver
        driver = webdriver.Chrome()
        
        options = Options()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)

index = 0
for item in chosen_headlines:
    url = summary_articles_df_title_and_url.loc[item]['url']
    # Open new browser and go to first URL
    driver.execute_script("window.open('');")
    #Open a new tab
    driver.switch_to.window(driver.window_handles[index])
    driver.get(url)
    index += 1


# #         # Assign URL
# #         #first_url = chosen_headlines[0]
# #         # first_url = summary_top_headlines_df_title_and_url.loc[chosen_headlines[0]]['url']
# #         # driver.get(first_url)
# #         index = 0
# #         for item in chosen_headlines:
# #             url = summary_top_headlines_df_title_and_url.loc[item]['url']
# #             # Open new browser and go to first URL
# #             driver.execute_script("window.open('');")
# #             #Open a new tab
# #             driver.switch_to.window(driver.window_handles[index])
# #             driver.get(url)
# #             index += 1
# #             # New Url
# #         #new_urls = [chosen_headlines[1:]]

        
# #         # Opening first url
# #         driver.get(first_url)
  
# #         #Open a new window
# #         # driver.execute_script("window.open('');")
  
# #         # #Switch to the new window and open new URL
# #         # driver.switch_to.window(driver.window_handles[1])
# #         # driver.get(new_urls[0])

# #         # driver.execute_script("window.open('');")
# #         # driver.switch_to.window(driver.window_handles[2])
# #         # driver.get(new_urls[1])
# #         #     # time.sleep(4)

  

