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

    
st.markdown("## 3. Find distribution of averge total_bill across each day by male and female")

 # load the data
df = pd.read_csv('./save_folder/tips.csv')


st.markdown('---')
 

features_to_groupby = ['day','gender']
feature = ['total_bill']
select_cols = feature+features_to_groupby
avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()
avg_total_bill = avg_total_bill.unstack()
# visual
fig, ax = plt.subplots()
avg_total_bill.plot(kind='bar',ax=ax)
ax.legend(loc='center left',bbox_to_anchor=(1.0,0.5))
st.pyplot(fig)

st.dataframe(avg_total_bill)