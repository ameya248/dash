import streamlit as st
import pandas as pd
#import plotly.express as px
st.title("Water Analysis")

#add a sidebar
st.sidebar.subheader("Visualisation Settings")
dataset=st.beta_container()
with dataset:

    st.header('lake dataset')

    HK_data = pd.read_csv('finalHK.csv')

    st.write(HK_data)
