from PIL import Image
import glob
import streamlit as st
from itertools import cycle

def app():
    st.title('Art Gallery')

    st.write('Enjoy this art gallery!')


    
filteredImages = ["C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//Dream.jpg",
                  "C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//love.jpg",
                 ] # your images here
caption = ["Dream", "Love"] # your caption here
cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(filteredImages):
    next(cols).image(filteredImage, width=150, caption=caption[idx])


