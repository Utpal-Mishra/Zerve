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
    st.title("Page 5: Steel Related Products")
    
    st.header("PART 5")
    
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
    
    dt = data[["Section", 'Trade Value']]
    dt = dt.groupby(['Section']).sum().reset_index()
        
    st.dataframe(dt)

    def barplot(data):
        fig = px.bar(data, x=dt.Section, y=dt['Trade Value'], color=dt.Section)
        fig.update_xaxes(title_text = "Steel Products", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
        # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
        fig.update_layout(height=600, width=1400, title_text='Trade Values for Steel Related Products') 
        st.plotly_chart(fig)
    
    barplot(dt) 
    
    dt = dt[["Section", 'Trade Value']].groupby("Section").sum()
    dt = dt.reset_index()
    fig = go.Figure(data=[go.Pie(labels=dt["Section"], values=dt['Trade Value'], hole=.5)])
    fig.update_layout(height=700, width=1400, title_text='Percentage Distribution of Trade Values for Steel Products') 
    st.plotly_chart(fig)
                    
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Animal Products"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Animal Products']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Animal Steel Products", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=900, width=1400, title_text='Trade Values for Animal Steel Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
        
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Animal Steel Products') 
        st.plotly_chart(fig)        
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Vegetable Products"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Vegetable Products']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Vegatable Steel Products", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=900, width=1400, title_text='Trade Values for Vegatable Steel Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
        
    
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Vegatable Steel Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Animal and Vegetable Bi-Products"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Animal and Vegetable Bi-Products']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Animal and Vegatable Steel Products", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=900, width=1400, title_text='Trade Values for Animal and Vegatable Steel Products') 
          st.plotly_chart(fig)
        
        barplot(dt)

        
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Animal and Vegatable Steel Products') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Foodstuffs"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Foodstuffs']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Food Steel Products", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=900, width=1400, title_text='Trade Values for Food Steel Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
        
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Food Steel Products') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Mineral Products"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Mineral Products']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)
        
        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Mineral Steel Products", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=900, width=1400, title_text='Trade Values for Mineral Steel Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
        
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Mineral Steel Products') 
        st.plotly_chart(fig)
    
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Chemical Products"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Chemical Products']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)
        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'])
          fig.update_xaxes(title_text = "Chemical Steel Products", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=2000, width=1400, title_text='Trade Values for Chemical Steel Products') 
          st.plotly_chart(fig)
        
        barplot(dt)

            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Plastics and Rubbers"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Plastics and Rubbers']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Plastics and Rubbers Products", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=700, width=1400, title_text='Trade Values for Plastics and Rubbers Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
            
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Plastic and Rubber Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox('Animal Hides'):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Animal Hides']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Animal Hide Products", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=1000, width=1400, title_text='Trade Values for Animal Hide Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
        
            
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Animal Hide Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Wood Products"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Wood Products']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Wood Products", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=700, width=1400, title_text='Trade Values for Wood Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
                    
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Wood Steel Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Paper Goods"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Paper Goods']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Paper Products", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=900, width=1400, title_text='Trade Values for Paper Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
              
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Paper Steel Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Textiles"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Textiles']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Textile Products", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=900, width=1400, title_text='Trade Values for Textile Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
        
                
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Textile Products')
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Footwear and Headwear"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Footwear and Headwear']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Footwear and Headwear Products", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=900, width=1400, title_text='Trade Values for Footwear and Headwear Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
                 
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Footwear and Headwear Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Stone and Glass"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Stone And Glass']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)
        
        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Stone and Glass Products", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=700, width=1400, title_text='Trade Values for Stone and Glass Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
    
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Stone and Glass Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Precious Metals"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Precious Metals']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)
        
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Precious Metal Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Metals"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Metals']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)
        
        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Metal Products", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=700, width=1400, title_text='Trade Values for Metal Products') 
          st.plotly_chart(fig)
        
        barplot(dt)

    
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Metal Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Machines"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Machines']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Machine Products", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=700, width=1400, title_text='Trade Percentage for Machine Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
            
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Machine Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Instruments"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Instruments']
        dt = dt.groupby(['HS2']).sum().reset_index()
        
        st.dataframe(dt)

        def barplot(data):
          fig = px.bar(dt, x=dt.HS2, y=dt['Trade Value'], color=dt.HS2)
          fig.update_xaxes(title_text = "Instrumental Products", rangeslider_visible=False, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'Trade Value', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=500, width=1400, title_text='Trade Values for Instrumental Products') 
          st.plotly_chart(fig)
        
        barplot(dt)
        
            
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for  Steel Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox("Miscellaneous"):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Miscellaneous']
        dt = dt.groupby(['HS2']).sum().reset_index()
                
        st.dataframe(dt)
        
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Miscellaneous Products') 
        st.plotly_chart(fig)
            
    ##########################################################################
    ##########################################################################
    
    if st.checkbox('Aet and Antiques'):
        dt = data[["Section", 'HS2', 'Trade Value']]
        dt = dt[dt["Section"] == 'Arts and Antiques']
        dt = dt.groupby(['HS2']).sum().reset_index()
                
        st.dataframe(dt)
        
        dt = dt[["HS2", 'Trade Value']].groupby("HS2").sum()
        dt = dt.reset_index()
        fig = go.Figure(data=[go.Pie(labels=dt["HS2"], values=dt['Trade Value'], hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='Trade Percentage for Art and Antiques Products') 
        st.plotly_chart(fig)
                    
    ##########################################################################
    ##########################################################################
    
    