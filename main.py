import streamlit as st
from utils.check_t import check_tick
from utils.check_t import create_fig



#st.set_page_config(layout="wide")
st.title("All in one Learning")

#st.write("Enter in a stock ticker")

user_input = st.text_input("Stock Ticker Input")
element_label = st.empty()

if user_input:
    element_label.write("Searching Stock Ticker!")
    tick, status = check_tick(user_input)
    element_label.write(status)

    if status == 'Found':
        
        fig = create_fig(tick)
        st.pyplot(fig)

    