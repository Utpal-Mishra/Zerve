import streamlit as st
import time

import sys
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import plotly.express as px

sys.setrecursionlimit(100000)
#print("Installed Dependencies")


def app():
    st.title("Page 3: India Steel Export")
    
    st.header("PART 3")
    
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
    
    data["Item - (Export Quantity in '000 Tonnes)"] = data["Item - (Export Quantity in '000 Tonnes)"].fillna('Unknown')
    data[['2013-14', '2014-15', '2015-16', '2016-17', '2017-18']] = data[['2013-14', '2014-15', '2015-16', '2016-17', '2017-18']].fillna(0)
  
    
    if st.checkbox("Show Cleaned DataFrame"):    
        st.dataframe(data)    
        
    ##########################################################################
    ##########################################################################
    
    st.subheader("Data Visualization: ITEMS")    
    
    # GROUP BY ITEMS
    dt = data[["Item - (Export Quantity in '000 Tonnes)", '2013-14', '2014-15', '2015-16', '2016-17', '2017-18']]
    dt = dt.melt(id_vars=["Item - (Export Quantity in '000 Tonnes)"], var_name = "Years", value_name = "Production")
    dt.sort_values(["Item - (Export Quantity in '000 Tonnes)", 'Years'], inplace = True)
    #dt
    
    def barplot(data):
      fig = px.bar(data, x=data["Item - (Export Quantity in '000 Tonnes)"], y=data.Production, animation_frame = data.Years, color=data["Item - (Export Quantity in '000 Tonnes)"])
      fig.update_xaxes(title_text = "Countries", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
      fig.update_yaxes(title_text = 'Steel Production (in Tons)', showline=True, linewidth=2, linecolor='black', mirror=True)
      # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
      fig.update_layout(height=700, width=1400, title_text='India Steel Items Production Export (2013-2018)') 
      st.plotly_chart(fig)

    if st.checkbox("Items: Bar Plot"): 
        barplot(dt)
    
    dt = dt[["Item - (Export Quantity in '000 Tonnes)", 'Production']].groupby("Item - (Export Quantity in '000 Tonnes)").sum()
    dt = dt.reset_index()
    
    def pieplot(data):
        fig = go.Figure(data=[go.Pie(labels=dt["Item - (Export Quantity in '000 Tonnes)"], values=dt.Production, hole=.5)])
        fig.update_layout(height=600, width=1400, title_text='India Steel Items Export Percentage (2013 - 2018)') 
        st.plotly_chart(fig)
        
    if st.checkbox("Items: Pie Plot"): 
        pieplot(data)
        
    ##########################################################################
    ##########################################################################
    
    st.subheader("Data Visualization: SUB-CATEGORIES")
    
    # GROUP BY SUB-CATEGORIES
    dt = data[["Sub-Category", '2013-14', '2014-15', '2015-16', '2016-17', '2017-18']]
    dt.groupby(['Sub-Category']).sum().reset_index()
    dt = dt.melt(id_vars=["Sub-Category"], var_name = "Years", value_name = "Production")
    dt.sort_values(["Sub-Category", 'Years'], inplace = True)
    #dt
    
    def barplot(data):
      fig = px.bar(data, x=data["Sub-Category"], y=data.Production, animation_frame = data.Years, color=data["Sub-Category"])
      fig.update_xaxes(title_text = "Sub-Categories", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
      fig.update_yaxes(title_text = 'Steel Production (in Tons)', showline=True, linewidth=2, linecolor='black', mirror=True)
      # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
      fig.update_layout(height=900, width=1400, title_text='India Steel Sub-Category Production Export (2013-2018)')  
      st.plotly_chart(fig)

    if st.checkbox("Sub-Categories: Bar Plot"): 
        barplot(dt)
    
    dt = dt[['Sub-Category', 'Production']].groupby('Sub-Category').sum()
    dt = dt.reset_index()
    
    def pieplot(data):
        fig = go.Figure(data=[go.Pie(labels=dt['Sub-Category'], values=dt.Production, hole=.5)])
        fig.update_layout(height=600, width=1400, title_text='India Steel Sub-Categories Export Percentage (2013 - 2018)')
        st.plotly_chart(fig)
        
    if st.checkbox("Sub-Categories: Pie Plot"): 
        pieplot(data)
        
    ##########################################################################
    ##########################################################################
    
    st.subheader("Data Visualization: CATEGORIES")
    
    # GROUP BY CATEGORES
    
    # GROUP BY SUB-CATEGORIES
    dt = data[["Category", '2013-14', '2014-15', '2015-16', '2016-17', '2017-18']]
    dt = dt.groupby(['Category']).sum().reset_index()
    dt = dt.melt(id_vars=["Category"], var_name = "Years", value_name = "Production")
    dt.sort_values(["Category", 'Years'], inplace = True)
    #dt
    def barplot(data):
      fig = px.bar(data, x=data["Category"], y=data.Production, animation_frame = data.Years, color=data["Category"])
      fig.update_xaxes(title_text = "Category", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
      fig.update_yaxes(title_text = 'Steel Production (in Tons)', showline=True, linewidth=2, linecolor='black', mirror=True)
      # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
      fig.update_layout(height=500, width=1000, title_text='India Steel Categories Export Percentage (2013-2018)') 
      st.plotly_chart(fig)

    if st.checkbox("Categories: Bar Plot"): 
        barplot(dt)
    
    dt = dt[['Category', 'Production']].groupby('Category').sum()
    dt = dt.reset_index()
    
    def pieplot(data):
        fig = go.Figure(data=[go.Pie(labels=dt.Category, values=dt.Production, hole=.5)])
        fig.update_layout(height=600, width=1400, title_text='India Steel Categories Export Percentage (2013 - 2018)') 
        st.plotly_chart(fig)
        
    if st.checkbox("Categories: Pie Plot"): 
        pieplot(data)
    
    ##########################################################################
    ##########################################################################
