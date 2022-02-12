

from PIL import Image
import glob
import streamlit as st
from itertools import cycle
import time
from multiapp import MultiApp
from apps import art_gallery

relevant_element = MultiApp()

def app():
    st.title('Art Gallery')

    st.write('Enjoy this art gallery!')

relevant_element.add_app("Home", art_gallery.app)
# relevant_element.add_app("Home", art_with_wombo.app)



# The main app
relevant_element.run()
    
Images = ["C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//Dream.jpg",
          "C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//love.jpg"
         ]

caption = ["Dream", "Love"] 

st.image(Images[0], width=350, caption=caption[0])


# index = 0 
# for image in Images:
#         im = Image.open(image)
#         st.image(im, caption=caption[index], width=350)
#         time.sleep(0)
#         index += 1 

# col1, col2 = st.columns(2)

# with col1:
#     st.header("A cat")
#     st.image(Images[0], caption=caption[0], width=350)

# with col2:
#     st.header("A dog")
#     st.image(Images[1], caption=caption[1], width=350)


