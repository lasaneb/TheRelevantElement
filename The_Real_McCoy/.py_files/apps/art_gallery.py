from PIL import Image
import glob
import streamlit as st

def app():
    st.title('Art Gallery')

    st.write('Enjoy this art gallery!')


    
    Images = "https://ipfs.io/ipfs/Qmd8xdaYVdPEwbtqRwAizfEcTaz35iS2XAYkVYm5esQdXV"

    caption = ["Dream", "Love"] 

    st.image(Images, width=350)

