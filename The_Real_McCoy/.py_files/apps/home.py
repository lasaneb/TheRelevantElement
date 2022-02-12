import streamlit as st

import time

def app():
    st.title('Home')

    st.write('In this app we will do cool stuff.')

# Image Carosel


    images = ["https://ipfs.io/ipfs/QmeTuPqzFWosFkCycvoN29jkfbMXDGWMMLMBMnStYXMW5W?filename=Dream.jpg",
              "https://ipfs.io/ipfs/QmNZAoco2BLbTnpqyBMmJ2CkH3ncoMbJofKWfRC9jX9UCy?filename=everything_is_awesome.jpg",
              "https://ipfs.io/ipfs/QmR1UCsrPNAUPKPtB133VtUMkyhTFLaqepmLnqkfahrHWU?filename=Family_and_Love.jpg"
             ]


    imageLocation = st.empty()
    for image in images:
        time.sleep(5)  # Pause for 5 seconds.
        imageLocation.image(image, width=350)



    



    

    