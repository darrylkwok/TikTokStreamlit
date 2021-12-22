import streamlit as st
import pandas as pd
# Import subprocess to run tiktok script from command line
from subprocess import call
import plotly.express as px


# Set page config
st.set_page_config(layout='wide')

# Create sidebar
st.sidebar.markdown("<div><img src='https://png2png.com/wp-content/uploads/2021/08/Tiktok-logo-png.png' width=100 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to analyse trending 📈 tiktoks using Python and Streamlit.")
st.sidebar.markdown("To get started <ol><li>Enter the <i>hashtag</i> you wish to analyse</li> <li>Click <i>Get Data</i>.</li> <li>Start analyzing</li></ol>",unsafe_allow_html=True)

# Input text box
hashtag = st.text_input("Search for a hashtag", value="")
# Submit button -> Triggered when clicked
if st.button('Get Data'):
    # Trigger the get data function
    call(['python', 'tiktok.py', hashtag])
    # Load in existing data for testing
    df = pd.read_csv("tiktokdata.csv")

    # Visualisation
    hist = px.histogram(df, x='desc', y='stats_diggCount', hover_data=['desc'], height=300)
    st.plotly_chart(hist, use_container_width=True)

    # Split cols
    left_col, right_col = st.columns(2)

    # Video stats chart
    scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # 
    scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)


    # Render the tabular dataframe
    df

