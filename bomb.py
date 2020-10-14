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
data_load_state = st.text('Loading data... It might take 45 secondes')
# Load 10,000 rows of data into the dataframe.
raw_data = load_data(1000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Data fully loaded! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(raw_data)

### loading bar ###

#'Starting to load data'	

## Add a placeholder
#latest_iteration = st.empty()
#bar = st.progress(0)

#for i in range(100):
#  # Update the progress bar with each iteration.
#  latest_iteration.text(f'Iteration {i+1}')
#  bar.progress(i + 1)
#  time.sleep(0.1)

#'...and now we\'re done!'

###

raw_data.dropna()
data = raw_data


data['latitude'] = data['latitude'].dropna()
data['longitude'] = data['longitude'].dropna()
data['country_flying_mission'].dropna()

#############################
#sidebar


Airforce = st.sidebar.multiselect('Airforce', data['country_flying_mission'].unique())

theater = st.sidebar.multiselect('theater', data['theater'].unique())

start_date = st.sidebar.date_input('start date', datetime.date(1939,1,1))
end_date = st.sidebar.date_input('end date', datetime.date(1949,1,1))

nan_drop = data[data['country_flying_mission'] == ' '].index
data.drop(nan_drop, inplace=True)


data['country_flying_mission']

##########

# Filter dataframe


new_df = data[(data['country_flying_mission'].isin(Airforce)) & (data['theater'].isin(theater))]



#####################
# Map

st.map(new_df)



######
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)
