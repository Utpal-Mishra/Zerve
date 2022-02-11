import streamlit as st
import time
import xlrd
import sys 
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import plotly.express as px

sys.setrecursionlimit(100000)
#print("Installed Dependencies")

def app():
    st.title("Page 1: Crude Steel")
    
    st.header("PART 1")
    
    st.subheader("Loading the COVID-19 Data....")
    
        
    file = st.file_uploader("Upload file")
    show_file = st.empty()
    
    if not file:
        show_file.info("Please upload a file of type: " + ", ".join([".csv", ".xls", ".xlsx"]))
        return
    
    label = st.empty()
    bar = st.progress(0)
    
    for i in range(100):
        # Update progress bar with iterations
        label.text(f'Loaded {i+1} %')
        bar.progress(i+1)
        time.sleep(0.01)
    
    path = file
    data = pd.read_excel(path)
    #print("Data Shape: ", data.shape)
    #data.head()
    
    ".... and now we're done!!!"
    
    if st.checkbox("Show DataFrame"):    
        # data
        st.dataframe(data)  
        
    ##########################################################################
    ##########################################################################
    
    st.subheader("Data Visualization")    
    
    # GROUP BY ITEMS
    data = data.melt(id_vars=["Country"], var_name = "Year", value_name = "Production")
    data.sort_values(["Country", 'Year'], inplace = True)
    data
    
    def barplot(data):
        fig = px.bar(data, x=data.Country, y=data.Production, animation_frame = data.Year, color=data.Country)
        fig.update_xaxes(title_text = "Countries", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Crude Steel Production (in Tons)', showline=True, linewidth=2, linecolor='black', mirror=True)
        # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=700, width=1400, title_text='Crude Steel Production (2017-2021)') 
        st.plotly_chart(fig)

    if st.checkbox("Items: Bar Plot"): 
        barplot(data)
    
            
    ##########################################################################
    ##########################################################################
