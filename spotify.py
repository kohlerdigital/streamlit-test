import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

###########################

st.title('Music popularity')
#MSNDATE-CORR = 'date/time'
DATA_URL = ('data/spotify_data.csv')

############################
#function

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

############################

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#############################
data['release_date_year'] = data.DatetimeIndex(data['release_date']).year


#########

filter_data = data['release_date']
st.markdown("release of stuff per year")
# bar chart 
st.bar_chart(filter_data)