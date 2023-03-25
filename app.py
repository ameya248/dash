import streamlit as st
import pandas as pd
import streamlit.components.v1 as components 
import numpy as np
import plotly.express as px
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objs as go
import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_option_menu as option_menu

with open('styles.css')as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#title
st.write("Water Quality Analysis of Bhopal Lakes", unsafe_allow_html = True, attributes = {"class": "waterQuality"})

#add a sidebar
st.sidebar.subheader("Visualisation Settings")

# add a select widget to the sidebar
chart_select = st.sidebar.selectbox(
    label = "Select the Lake",
    options = ['Hathaikheda dam', 'Sarangpani lake', 'Upper lake']
)
if chart_select == 'Hathaikheda dam':
      df = pd.read_csv('finalHK.csv')
      st.subheader('Hathaikheda dam')
elif chart_select == 'Sarangpani lake' :
     df = pd.read_csv('final-new.csv')
     st.subheader('Sarangpani lake')
elif chart_select == 'Upper lake' :
     df = pd.read_csv('finalHK.csv')
     st.subheader('Upper Lake')


global numeric_columns
try:
    st.write(df.head())
    numeric_columns  = list(df.select_dtypes(['float','int' ]).columns)
except Exception as e:
    print(e)

   

    

# add a select widget to the sidebar
chart_select = st.sidebar.selectbox(
    label = "Select the Chart Type",
    options = ['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
)

if chart_select == 'Scatterplots':
    st.sidebar.subheader('Scatterplot Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.scatter(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Lineplots':
    st.sidebar.subheader('Lineplots Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.area(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader('Boxplot Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.box(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Histogram':
    st.sidebar.subheader('Histogram Settings')
    try:
        x_values = st.sidebar.selectbox('Select the variable to plot histogram', options = numeric_columns)
        bins = st.sidebar.slider("Select the number of bins", min_value=5, max_value=50, value=20, step=1)
        plot = px.histogram(data_frame = df, x = x_values, nbins=bins)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

