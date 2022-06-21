import streamlit as st
from formula.relativity import relativity as REL

def RelativityApp():
  st.write("## Relativity Applet")
  number = st.slider('Select a number', 0.0, 100.0, 50.0)

