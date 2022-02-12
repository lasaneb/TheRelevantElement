from PIL import Image
import glob
import streamlit as st


st.title('Art Gallery')

st.write('Enjoy this art gallery!')

image = Image.open("C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//Dream.jpg")

st.image(image, caption="Dream", use_column_width=True)


# images = []
# for filename in glob.glob("C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images"):
#     images.append(Image.open(filename))

# image = Image.open(images)
# st.image(image, use_column_width=True)