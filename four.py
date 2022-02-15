import streamlit as st
import time
import sys 
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

sys.setrecursionlimit(100000)
#print("Installed Dependencies")



def app():
    st.title("Page 4: Steel Tariff Data")
    
    st.header("PART 4")
    
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
    data = pd.read_csv(path)
    #print("Data Shape: ", data.shape)
    #data.head()
    
    ".... and now we're done!!!"
    
    if st.checkbox("Show DataFrame"):    
        # data
        st.dataframe(data)  
        
    ##########################################################################
    ##########################################################################
    
    st.subheader("Data Visualization")    
    
    if st.checkbox("Tariff in 2002"):
        dt = data[data['Year'] == 2002]
        dt = dt.groupby(['Country']).sum().reset_index()
        
        st.dataframe(dt)

        fig = px.scatter(dt, x=dt.Country, y=dt.Tariff, color=dt.Country, size=dt.Tariff)
        fig.update_xaxes(title_text = "Country", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Tariff %', showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=500, width=1000, title_text='Global Tariff % in 2002') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Tariff in 2003"):
        dt = data[data['Year'] == 2003]
        dt = dt.groupby(['Country']).sum().reset_index()
        
        st.dataframe(dt)

        fig = px.scatter(dt, x=dt.Country, y=dt.Tariff, color=dt.Country, size=dt.Tariff)
        fig.update_xaxes(title_text = "Country", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Tariff %', showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=500, width=1000, title_text='Global Tariff % in 2003') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Tariff in 2013"):
        dt = data[data['Year'] == 2013]
        dt = dt.groupby(['Country']).sum().reset_index()
        
        st.dataframe(dt)

        fig = px.scatter(dt, x=dt.Country, y=dt.Tariff, color=dt.Country, size=dt.Tariff)
        fig.update_xaxes(title_text = "Country", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Tariff %', showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=500, width=1000, title_text='Global Tariff % in 2013') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Tariff in 2015"):
        dt = data[data['Year'] == 2015]
        dt = dt.groupby(['Country']).sum().reset_index()
        
        st.dataframe(dt)

        fig = px.scatter(dt, x=dt.Country, y=dt.Tariff, color=dt.Country, size=dt.Tariff)
        fig.update_xaxes(title_text = "Country", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Tariff %', showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=500, width=1000, title_text='Global Tariff % in 2015') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Tariff in 2016"):
        dt = data[data['Year'] == 2016]
        dt = dt.groupby(['Country']).sum().reset_index()
        
        st.dataframe(dt)

        fig = px.scatter(dt, x=dt.Country, y=dt.Tariff, color=dt.Country, size=dt.Tariff)
        fig.update_xaxes(title_text = "Country", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Tariff %', showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=500, width=1000, title_text='Global Tariff % in 2016') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Tariff in 2017"):
        dt = data[data['Year'] == 2017]
        dt = dt.groupby(['Country']).sum().reset_index()
        
        st.dataframe(dt)

        fig = px.scatter(dt, x=dt.Country, y=dt.Tariff, color=dt.Country, size=dt.Tariff)
        fig.update_xaxes(title_text = "Country", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Tariff %', showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=500, width=1000, title_text='Global Tariff % in 2017') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Tariff in 2018"):
        dt = data[data['Year'] == 2018]
        dt = dt.groupby(['Country']).sum().reset_index()
        
        st.dataframe(dt)

        fig = px.scatter(dt, x=dt.Country, y=dt.Tariff, color=dt.Country, size=dt.Tariff)
        fig.update_xaxes(title_text = "Country", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Tariff %', showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=500, width=1000, title_text='Global Tariff % in 2018') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Tariff in 2019"):
        dt = data[data['Year'] == 2019]
        dt = dt.groupby(['Country']).sum().reset_index()
        
        st.dataframe(dt)

        fig = px.scatter(dt, x=dt.Country, y=dt.Tariff, color=dt.Country, size=dt.Tariff)
        fig.update_xaxes(title_text = "Country", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Tariff %', showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=500, width=1000, title_text='Global Tariff % in 2019') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
