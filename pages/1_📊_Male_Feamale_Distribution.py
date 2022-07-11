from re import L
import streamlit as st 
import pandas as pd
import numpy as np
# static
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard", page_icon="📊")

query_params = st.experimental_get_query_params()
 

 
if query_params:
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
            section[data-testid="stSidebar"]  {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    my_id =  query_params.get("id")[0]

    st.write(my_id)
    st.balloons()
else:
     hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
     st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
     
 

st.markdown("# Male and Female distribution")
 
 # load the data
df = pd.read_csv('./save_folder/tips.csv')
    
  
 
st.markdown('---')
with st.container(): 
    st.write('1. Find number of Male and Female distribution (pie and bar)')
    value_counts = df['gender'].value_counts()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Pie Chart')    
        # draw pie chart
        fig,ax = plt.subplots()
        ax.pie(value_counts,autopct='%0.2f%%',labels=['Male','Female'])
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
   
