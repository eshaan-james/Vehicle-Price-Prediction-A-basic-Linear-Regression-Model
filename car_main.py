import streamlit as st
import pandas as pd
import car_home
import car_models
import car_plots
# Configure your home page by setting its title and icon that will be displayed in a browser tab.
st.set_page_config(page_title='Car Price Prediction',
                   page_icon='random',
                   layout='wide',
                   initial_sidebar_state='auto'
                   )


# Loading the dataset.
@st.cache_data()
def load_data():
    df = pd.read_csv("car data.csv")
    return df

car_df = load_data()

st.title('Car Price Prediction')
pages_dict = {"Home": car_home,
              "Classification": car_models,
              "Plots": car_plots}

st.sidebar.title('Navigation')
user_choice = st.sidebar.radio('Go To', tuple(pages_dict.keys()))
selected_page = pages_dict[user_choice]
selected_page.app(car_df)