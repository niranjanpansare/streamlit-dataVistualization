from re import L
import streamlit as st 
import pandas as pd
import numpy as np
# static
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard", page_icon="📊")
st.markdown("## 2. Find distribution of Male and Female spent")

 # load the data
df = pd.read_csv('./save_folder/tips.csv')
    
  
# streamlit widgets and charts     
data_types = df.dtypes
cat_cols = tuple(data_types[data_types == 'object'].index)

st.markdown('---')
with st.container(): 
    feature = st.selectbox('Select the feature you want to display bar and pie chart',
                           cat_cols
                           )
    value_counts = df[feature].value_counts()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Pie Chart')    
        # draw pie chart
        fig,ax = plt.subplots()
        ax.pie(value_counts,autopct='%0.2f%%',labels=value_counts.index)
        st.pyplot(fig)
        
    with col2:
        st.subheader('Bar Chart')
        # draw bar plot
        fig,ax = plt.subplots()
        ax.bar(value_counts.index,value_counts)
        st.pyplot(fig)
    
    # put this in expander
    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)
 