# Initial Imports

import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from helium import *
import time



def app():
    st.title('Speech Recognition')


    st.write('Speech recognition software is used to capture speech and search for top results')

    show_elements = []

    # Initialize the speech recognition engine

# Set the microphone to listen to the user and convert the audio to text; no set time limit

    if st.button('Start Listening'):
        def get_audio():
            r = sr.Recognizer()
            with sr.Microphone() as source:

                audio = r.listen(source)
                said = ""

            try:
                said = r.recognize_google(audio)
            
            except Exception as e:
                print("Exception:" + str(e))

            return said
    
        element = get_audio()
    
        show_elements.append(element)

        st.write("The Current Element")
        st.write(element)

        if st.button('Online Search'):
            st.spinner('Searching for' + element)
            helium.start_chrome('https://www.google.com/search?q=' + element)
        

