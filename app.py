import streamlit as st
import pandas as pd
import streamlit.components.v1 as components 
import numpy as np
import plotly.express as px
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objs as go


with st.sidebar:
    selected = option_menu.option_menu(
        menu_title = "Main Menu",
        options = ["Home", "EDA"]
    )
#add a sidebar
st.sidebar.subheader("Visualisation Settings")
dataset=st.beta_container()
with dataset:

    st.header('lake dataset')

    HK_data = pd.read_csv('finalHK.csv')

    st.write(HK_data)
