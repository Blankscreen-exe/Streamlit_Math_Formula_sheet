import streamlit as st

import RelativityApp as RELapp
# import Euler as EULapp
# import EulerIdentitiy as EULIDapp
# import Quadratic as QUAapp
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
    EULIDapp.EulerIdentityApp()
  except:
    st.error("Something went wrong in Euler identity App")