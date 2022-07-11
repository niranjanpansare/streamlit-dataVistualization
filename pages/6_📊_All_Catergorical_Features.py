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

    
st.markdown("## 4. All catergorical Faetures")

 # load the data
df = pd.read_csv('./save_folder/tips.csv')

# streamlit widgets and charts     
data_types = df.dtypes
cat_cols = tuple(data_types[data_types == 'object'].index)
### 
with st.container():
    # 1. include all categorical features (multiselect)
    # 2. bar, area, line (selectbox)
    # 3. stacked (radio)
    c1, c2 , c3 = st.columns(3)
    with c1:
        group_cols = st.multiselect('select the features',cat_cols,cat_cols[0])
        features_to_groupby = group_cols
        n_features = len(features_to_groupby)
    
    with c2:
        chart_type = st.selectbox('Select Chart type',
                                  ('bar','area','line'))
        
    with c3:
        stack_option = st.radio('Stacked',('Yes','No'))
        if stack_option == 'Yes':
            stacked = True
        else:
            stacked = False
            

    feature = ['total_bill']
    select_cols = feature+features_to_groupby
    avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()
    if n_features >1:
        for i in range(n_features-1):
            avg_total_bill = avg_total_bill.unstack()
            
    avg_total_bill.fillna(0,inplace=True)
    
    # visual
    fig, ax = plt.subplots()
    avg_total_bill.plot(kind=chart_type,ax=ax,stacked=stacked)
    ax.legend(loc='center left',bbox_to_anchor=(1.0,0.5))
    ax.set_ylabel('Avg Total Bill')
    st.pyplot(fig)

    with st.expander('click here to display values'):
        st.dataframe(avg_total_bill)
        