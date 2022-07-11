import streamlit as st 
import pandas as pd 
import numpy as np
import os 



st.set_page_config(page_title="Simple App", page_icon="🏠")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.container():    
    uploaded_file = st.file_uploader('Choose a file')
    save_button = st.button('save file')
    if save_button:
        if uploaded_file is not None:
            with open(os.path.join("./save_folder",uploaded_file.name),mode='wb') as f:
                f.write(uploaded_file.getbuffer())
                
            st.success('File uploaded sucessfully')
            
        else:
            st.warning('Please select the file you want to upload')


with st.container():    
    df = pd.read_csv('./save_folder/tips.csv')

    # st.dataframe to display dataframes

    st.header('Dataframe')
    st.caption('Display a dataframe as an interactive table')

    st.dataframe(data=df,width=2000,height=500)

   
