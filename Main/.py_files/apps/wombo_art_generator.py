#Initial Imports


from helium import *
import shutil
import time
from selenium import webdriver
import streamlit as st
from random import randint
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
import requests
from pathlib import Path
import pandas as pd
import re
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

def app():

# Function to create wombo art
        def create_wombo_art(description, title, art_style):

            helium.start_chrome('https://app.wombo.art')
            helium.write(description, into="Type anything")
            helium.click(Image(alt = art_style))
            helium.click("Create")
            helium.wait_until(Text("Name artwork").exists,timeout_secs=60)
            title = title.replace(" " , "_") 
            helium.write(title, into="Enter title")
            helium.click("Save")
            time.sleep(10)
            original = r"C://Users//Airma//Downloads//" + title + "_TradingCard.jpg"
            target = r"C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//Main//resources//Images//WomboArtWorks//" + title + ".jpg"
            shutil.move(original,target)
            helium.kill_browser()
    
            return title

            newsapi = NewsApiClient(api_key="6979450998b44ae483661232ae2c1fd3")
            top_articles = newsapi.get_top_headlines(country="us", language='en')

            return top_articles

            top_headlines_df = pd.DataFrame.from_dict(top_headlines()['articles'])
            top_headlines_df["source"] = top_headlines_df["source"].apply(lambda x: x['name'])

        art_styles = ["Moonwalker", 
                "Blacklight", 
                "Baroque", 
                "Etching", 
                "S.Dali", 
                "Wuhtercuhler", 
                "Provenance", 
                "Rose Gold",  
                "Mystical",
                "Festive",
                "Dark Fantasy",
                "Psychic",
                "Pastel",
                "HD",
                "Vibrant",
                "Fantasy Art",
                "Steampunk",
                "Ukiyoe",
                "Synthwave",
    ]

        random_int_style = randint(0, len(art_styles) - 1)
        description = st.text_input("Enter description")
        title = st.text_input("Enter title")
        
        if st.button("Generate Art"):
            st.write("Generating Art with Wombo...")
            create_wombo_art(description, title, art_styles[random_int_style])
            time.sleep(5)
            st.image("C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//Main//resources//Images//WomboArtWorks//" + title + ".jpg")
            #st.image(r"C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//WomboArtWorks//" + title + ".jpg", width=350)
            st.success("Art Generated!")

            
        # Generate an Art from random words
        if st.button("I Feel Lucky"):
            st.spinner("Randomizing...")
            time.sleep(2)
            st.spinner("Generating Art with Wombo...")
            time.sleep(2)

            
            response = requests.get(word_site)
            WORDS = response.content.splitlines()
            
            useable_words = []

            for word in WORDS:
                if len(word) > 5 and len(word) < 12:
                    useable_words.append(word)     

            random_word = str(useable_words[randint(0, len(useable_words) - 1)]).lower()

            create_wombo_art(random_word, 
                            random_word, 
                            art_styles[random_int_style]) 

        # Generate an Art from headlines
        if st.button("Generate from an article"):
            st.spinner("Randomizing...")
            time.sleep(2)
            st.spinner("Generating Art with Wombo...")
            time.sleep(2)

            # Load all articles
            csv = Path("all_relevant_articles.csv")
            summary_articles_df = pd.read_csv(csv)
            random_number = randint(0, len(summary_articles_df) - 1)

            
            random_article = re.split('\s+', summary_articles_df.iloc[random_number]['title'])
            word_one_from_article = random_article[randint(0, len(random_article) - 1)]
            word_two_from_article = random_article[randint(0, len(random_article) - 1)]
            word_three_from_article = random_article[randint(0, len(random_article) - 1)]
            random_int_style = randint(0, len(art_styles) - 1)
            
            create_wombo_art(word_one_from_article + " " 
                            + word_two_from_article + " " 
                            + word_three_from_article, 
                            word_one_from_article,
                            art_styles[random_int_style])



