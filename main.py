import streamlit as st

import RelativityApp as RELapp
import EulerApp as EULapp
# import EulerIdentitiy as EULIDapp
import QuadraticApp as QUAapp
import Quadratic2App as QUA2app
# import QuadraticEq as QUAEQapp

st.write("# Math Formula App")
options = ["Relativity","Euler Identity","Quadratic Equation","Quadratic"]
app = st.selectbox("Select a Formula to run", options)

if app == options[0]:
  try:
    RELapp.RelativityApp()
  except:
    st.error("Something went wrong in Relativity App")
elif app == options[1]:
  try:
    EULapp.Euler()
  except:
    st.error("Something went wrong in Euler identity App")
elif app == options[2]:
  try:
    QUAapp.Quadratic()
  except:
    st.error("Something went wrong in Quadratic App")
elif app == options[3]:
  try:
    QUA2app.Quadratic()
  except:
    st.error("Something went wrong in Quadratic 2 App")