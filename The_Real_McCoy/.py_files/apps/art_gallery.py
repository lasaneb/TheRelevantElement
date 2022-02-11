from PIL import Image
import glob
import streamlit as st

def app():
    st.title('Art Gallery')


    st.write('Enjoy this art gallery!')


images = glob.glob("C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images")
index= st.number_input('Index')

if st.button('Next'):
    index += 1


if st.button('Prev'):
    if index > 0:
        index = index -1

image = Image.open(images[index])
st.image(image, use_column_width=True)


