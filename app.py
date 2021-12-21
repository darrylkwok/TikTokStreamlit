import streamlit as st
import pandas as pd

# Input text box
hashtag = st.text_input("Search for a hashtag", value="")
# Submit button -> Triggered when clicked
if st.button('Get Data'):
    # Trigger the get data function
    st.write(hashtag)

# Load in existing data for testing
df = pd.read_csv("tiktokdata.csv")

# Render the tabular dataframe
df