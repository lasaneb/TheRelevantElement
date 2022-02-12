import requests
import json
import pandas as pd
from random import randint
import streamlit as st

@st.cache
def app():
    st.title('Inspiring Quotes')

    st.write('In this app we will inspire you to do cool stuff.')

#Get inspiring Quotes
    url = "https://inspiring-quotes.p.rapidapi.com/multiple"

    querystring = {"count":"50"}

    headers = {
        'x-rapidapi-host': "inspiring-quotes.p.rapidapi.com",
        'x-rapidapi-key': "2075772920msh129b70e8d2ba5a2p1048b0jsn1be03d3f1b6d"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    results = (response.text)

    results = json.loads(results)

    results = pd.DataFrame(results)

    inspiring_quotes = results['data'][0:len(results['data'])]

    st.button('Get Inspiring Quote')

    random_int = randint(0, len(inspiring_quotes))

    quote = results['data'][random_int]['quote']
    author = results['data'][random_int]['author']

    inspiring_quote = f"{quote} - {author}"

    st.write(inspiring_quote)