from re import L
import streamlit as st 
import pandas as pd
import numpy as np
# static
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(page_title="Dashboard", page_icon="📊")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    
st.markdown("## 5. Find the relation between total_bill and tip on time (scatter plot)")

 # load the data
df = pd.read_csv('./save_folder/tips.csv')

# streamlit widgets and charts     
data_types = df.dtypes
cat_cols = tuple(data_types[data_types == 'object'].index)


st.markdown('---')
 

fig, ax = plt.subplots()
hue_type = st.selectbox('Select the feature to hue',cat_cols)

sns.scatterplot(x='total_bill',y='tip',hue=hue_type,ax=ax,data=df)
st.pyplot(fig)