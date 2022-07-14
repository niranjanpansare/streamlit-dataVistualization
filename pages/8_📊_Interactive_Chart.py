 
import streamlit as st 
import pandas as pd 
import numpy as np

# plotly
import plotly.express as px


st.set_page_config(page_title="Dashboard", page_icon="📊")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #symbol {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


 # load the data
df = pd.read_csv('./save_folder/tips.csv')

# streamlit widgets and charts     
data_types = df.dtypes
cat_cols = tuple(data_types[data_types == 'object'].index)

st.subheader("Interactive Chart")
path = st.multiselect('select the categorical features path',
                      (cat_cols))
fig = px.sunburst(data_frame=df,path=path)
st.plotly_chart(fig)
