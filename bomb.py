import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

###########################
#load data

st.title('ww2 bombings')
#DATA_URL = ('https://query.data.world/s/sl4ylhcarpfsvgfc6ets4ufs4itgbm')
DATA_URL = ('data/THOR_WWII_DATA_CLEAN.csv')


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
data = load_data(1000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

if st.sidebar.checkbox('Show raw data'):
    st.sidebar.subheader('Raw data')
    st.sidebar.write(data)
#############################
#sidebar


Airforce = st.sidebar.multiselect('Airforce', data['country_flying_mission'].unique())

theater = st.sidebar.multiselect('theater', data['theater'].unique())


 ##########


# Filter dataframe
new_df = data[(data['country_flying_mission'].isin(Airforce)) & (data['theater'].isin(theater))]

# write dataframe to screen
st.write(new_df)


new_df['latitude'] = data['latitude'].dropna().apply(np.int64)
new_df['longitude'] = data['longitude'].dropna().apply(np.int64)

new_df['latitude']

st.map(data)