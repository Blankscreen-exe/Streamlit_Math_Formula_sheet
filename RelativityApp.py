import streamlit as st
from formula.Relativity import relativity as app

def RelativityApp():
  st.write("## Relativity Applet")
  number1 = st.slider('Select a number', 0.0, 100.0, 50.0,key=1)
  number2 = st.slider('Select a number', 0.0, 100.0, 50.0,key=2)
  st.write(f"## E = {app(number1,number2)}")

