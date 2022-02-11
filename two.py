import streamlit as st
import time
import xlrd
import sys 
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from datetime import datetime as dt

sys.setrecursionlimit(100000)
#print("Installed Dependencies")

 #!conda install -c conda-forge geopy --yes 
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values
        
#!conda install -c conda-forge folium=0.5.0 --yes
import folium # plotting library
from folium import plugins
from streamlit_folium import folium_static
#from streamlit_folium import folium_static


def app():
    st.title("Page 2: Past Steel Data")
    
    st.header("PART 2")
    
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
    
    data = data.fillna(0)
    data = data[data.irst > 0]
    
    Country = []
    Longitude = []
    Latitude = []
    
    for i in data.stateabb.unique():
      geolocator = Nominatim(user_agent="four_square")
      location = geolocator.geocode(i)
      latitude = location.latitude
      longitude = location.longitude
      Country.append(i)
      Longitude.append(longitude)
      Latitude.append(latitude)
      # print(i, longitude, latitude)
    
    # data["Longitude"] = Longitude
    # data["Latitude"] = Latitude
    
    Coordinates = pd.DataFrame({"stateabb": Country,
                   "Longitude": Longitude,
                   "Latitude": Latitude})
    
    if st.checkbox("Show Coordinates DataFrame"):    
        # data
        st.dataframe(Coordinates)
        
        
    newdata = pd.merge(data, Coordinates, on='stateabb', how='inner')
    
    st.subheader("Data Visualization")    
    
    def map(data):
      fig = px.scatter_geo(newdata, 
                         lat='Latitude', 
                         lon='Longitude', 
                         size=data['irst'], 
                         animation_frame="year", 
                         animation_group = "stateabb",
                         title='IRON AND STEEL PRODUCTION (1816 - 2007)', 
                         hover_name="stateabb",
                         projection = "orthographic", 
                         width = 1400,
                         height = 600, 
                         color = "stateabb")
      fig.update(layout_coloraxis_showscale=False)
      st.plotly_chart(fig)
        

    if st.checkbox("Orthographic Plot"): 
        map(newdata)
    
            
    ##########################################################################
    ##########################################################################

    newdata['irst_max'] = newdata.groupby(['year'])['irst'].transform(max)
    maxdata = newdata[newdata['irst'] == newdata['irst_max']][['stateabb', 'year', 'irst_max']]
    
    if st.checkbox("Maximum Steel Production"): 
        fig = px.scatter(maxdata, x="year", y="irst_max", size="irst_max", color="stateabb", hover_name="stateabb")
        fig.update_xaxes(title_text = "YEAR", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "IRON AND STEEL MAX PRODUCTION (in tons)", showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=700, width=1400, title_text="STATES WITH MAX PRODUCTION OF IRON AND STEEL (1816 - 2007)") 
        st.plotly_chart(fig)
    
    
    ##########################################################################
    ##########################################################################
    
    newdata['irst_min'] = newdata.groupby(['year'])['irst'].transform(min)
    mindata = newdata[newdata['irst'] == newdata['irst_min']][['stateabb', 'year', 'irst_min']]
    
    if st.checkbox("Mininum Steel Production"):
        fig = px.scatter(mindata, x="year", y="irst_min", size="irst_min", color="stateabb", hover_name="stateabb")
        fig.update_xaxes(title_text = "YEAR", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_yaxes(title_text = "IRON AND STEEL MAX PRODUCTION (in tons)", showline=True, linewidth=2, linecolor='black', mirror=True)
        fig.update_layout(height=700, width=1400, title_text="STATES WITH MAX PRODUCTION OF IRON AND STEEL (1816 - 2007)") 
        st.plotly_chart(fig)