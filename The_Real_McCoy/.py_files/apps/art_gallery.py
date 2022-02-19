from PIL import Image
import glob
import streamlit as st

def app():
    st.title('Art Gallery')

    st.write('Enjoy this art gallery!')



    col1, col2, col3, col4, col5 = st.columns(5)
    image_list = []
    for filename in glob.glob('C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//WomboArtWorks//*.jpg'): # Gets only jpg files
        im=Image.open(filename)
        image_list.append(im)

    with col1:

        st.image(image_list[0:10], width=250)

    with col3:
        st.image(image_list[11:20], width=250)

    with col5:
        st.image(image_list[21:30], width=250)

 

