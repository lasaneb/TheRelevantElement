# Streamlit Interface

import streamlit as st


# from dataclasses import dataclass
# from typing import Any, List
# import os
# from newsapi import NewsApiClient
# from newsapi.newsapi_client import NewsApiClient
# from datetime import date, timedelta
# import pandas as pd
# import pdfkit
# import flair
#news_api_key = os.getenv("news_api_key")

# st.markdown("# Top Headlines")
import streamlit as st
import numpy as np
import pandas as pd
import sklearn
from sklearn import datasets

def app():
    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns = iris.feature_names)
    Y = pd.Series(iris.target, name = 'class')
    df = pd.concat([X,Y], axis=1)
    df['class'] = df['class'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

    st.write(df)

# Define a function to retrieve top headlines for Country USA

# def top_headlines():
#     newsapi = NewsApiClient(api_key=st.secrets["news_api_key"])
#     top_articles = newsapi.get_top_headlines(country="us", language='en')

#     return top_articles

#top_headlines = pd.DataFrame(app()['articles']) 

#st.write(top_headlines)