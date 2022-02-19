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

        st.image(image_list[0:30], width=275)



    with col5:
        st.image(image_list[31:60], width=275)

 

