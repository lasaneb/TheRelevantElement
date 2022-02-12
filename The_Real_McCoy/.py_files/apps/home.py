import streamlit as st

def app():
    st.title('Home')

    st.write('In this app we will do cool stuff.')

    images = ["https://ipfs.io/ipfs/QmeTuPqzFWosFkCycvoN29jkfbMXDGWMMLMBMnStYXMW5W?filename=Dream.jpg",
              "https://ipfs.io/ipfs/QmNZAoco2BLbTnpqyBMmJ2CkH3ncoMbJofKWfRC9jX9UCy?filename=everything_is_awesome.jpg",
              "https://ipfs.io/ipfs/QmR1UCsrPNAUPKPtB133VtUMkyhTFLaqepmLnqkfahrHWU?filename=Family_and_Love.jpg"
    ]

    imageLocation = st.empty()

    imageLocation.image(images[0], width=350)

    imageLocation.image(images[1], width=350)

    if st.button('Stop'):
        imageLocation.image(images[1], width=350)

    # def image_carosel(images):
    #     for image in images:
    #         st.image(image, width=350)

    # image_carosel(images)


    

    