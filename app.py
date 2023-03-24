import streamlit as st
import pandas as pd
import streamlit.components.v1 as components 
import numpy as np
import plotly.express as px
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objs as go


    
lakes_options = ["Lendiya", "Nawab Munshi Hussain Khan", "Kerwa Dam"]
if selected == "Home":
    st.header('__Monitoring the water quality of Bhopal Region using Image processing and other GIS techniques__ ')
    st.subheader('Introduction : ')

elif selected == "EDA":
    st.markdown("""<h style="color:#e60000;font-size:45px;font-weight:bolder;"><u>EXPLORATORY DATA ANALYSIS</u></h>""",unsafe_allow_html=True)
    st.write("**Exploratory Data Analysis (EDA)** is an approach to analyze the data using visual techniques. It is used to discover trends, patterns, or to check assumptions with the help of statistical summary and graphical representations. \n\n Here we have explored various parameters of lakes and came up with the interesting EDAs of the follwing ")
    option = st.selectbox(label='**Lakes**', options=lakes_options)
    
    if 'Lendiya' in option:
        st.write("")
#add a sidebar
st.sidebar.subheader("Visualisation Settings")
dataset=st.beta_container()
with dataset:

    st.header('lake dataset')

    HK_data = pd.read_csv('finalHK.csv')

    st.write(HK_data)
