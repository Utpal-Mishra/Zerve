import home
import one 
import two
import three
import four
import five
#import status

import streamlit as st

st.audio(open('inspire.mp3', 'rb').read(), format='audio/ogg')

PAGES = {
    "Home": home,
    "Crude Steel": one,
    "Past Steel Data": two,
    "India Steel Export": three,
    "Steel Tariff Data": four,
    "Steel Related Products": five,
    #"Find Weather Status": status
}

st.sidebar.title('Navigation Bar')

selection = st.sidebar.selectbox("Go to: \n", list(PAGES.keys()))
page = PAGES[selection]
page.app()