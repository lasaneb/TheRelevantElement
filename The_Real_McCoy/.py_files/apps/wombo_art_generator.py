#Initial Imports


from helium import *
import shutil
import time
from selenium import webdriver
import streamlit as st
from random import randint
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient

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
            target = r"C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//WomboArtWorks//" + title + ".jpg"
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

        random_int_style = randint(0, len(art_styles))
        description = st.text_input("Enter description")
        title = st.text_input("Enter title")
        
        if st.button("Generate Art"):
            st.write("Generating Art with Wombo...")
            create_wombo_art(description, title, art_styles[random_int_style])
            time.sleep(5)
            st.image("C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//WomboArtWorks//" + title + ".jpg", width=350)
            st.success("Art Generated!")
