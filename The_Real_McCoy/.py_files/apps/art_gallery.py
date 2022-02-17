from PIL import Image
import glob
import streamlit as st

def app():
    st.title('Art Gallery')

    st.write('Enjoy this art gallery!')



    col1, col2, col3 = st.columns(4)
    image_list = []
    for filename in glob.glob('C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//WomboArtWorks//*.jpg'): # Gets only jpg files
        im=Image.open(filename)
        image_list.append(im)

    st.image(image_list, width=300)

