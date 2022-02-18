#Initial Imports


from helium import *
import shutil
import time
from selenium import webdriver
import streamlit as st
from random import randint

# Function to get wombo art
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

random_int = randint(0, len(art_styles))

if st.button("Generate Art"):
    description = st.text_input("Enter description")
    title = st.text_input("Enter title")
    st.write("Generating Art with Wombo...")
    title = create_wombo_art("This is a test", "Test", art_styles[random_int])
    st.image(r"C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//WomboArtWorks//" + title + ".jpg", width=350)
    st.write("Art Generated!")
