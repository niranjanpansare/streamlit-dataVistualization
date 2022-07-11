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

    
st.markdown("## 2. Find distribution of Male and Female spent")

 # load the data
df = pd.read_csv('./save_folder/tips.csv')
    
    ## 2. Find distribution of Male and Female spent
st.markdown('---')
with st.container():
     
    # box, violin, kdeplot, histogram
    chart = ('box','violin','kdeplot','histogram')
    chart_selection = st.selectbox('Select the chart type',chart)
    fig , ax = plt.subplots()
    if chart_selection == 'box':
        sns.boxplot(x='gender',y='total_bill',data=df,ax=ax)
    elif chart_selection == 'violin':
        sns.violinplot(x='gender',y='total_bill',data=df,ax=ax)
    elif chart_selection == 'kdeplot':
        sns.kdeplot(x=df['total_bill'],hue=df['gender'],ax=ax,shade=True)
    else:
        sns.histplot(x='total_bill',hue='gender',data=df,ax=ax)
    
    st.pyplot(fig)