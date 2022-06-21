import streamlit as st
from formula.quadratic import Quadratic as app

def Quadratic():
  st.write("## Quadratic  Applet")
  number1 = st.slider('Select a number', 0.0, 100.0, 50.0,key=1)
  number2 = st.slider('Select a number', 0.0, 100.0, 50.0,key=2)
  number3 = st.slider('Select a number', 0.0, 100.0, 50.0,key=3)
  st.write(f"## Output =")
  st.write(app(number1,number2,number3))