import streamlit as st

st.write("Hello welcome to Quiz Game application he")
st.sidebar.markdown("Quiz Menu...")
st.sidebar.markdown("Quiz Game")
score = 0
st.write("Q1. Which is the first alphabet of english language?\nA) c   B) d    C) a   D) f")
ans = st.text_input("Enter your choice...")
if ans == 'c' or ans=='C':
  score=5
else:
  score = 0
st.write("Q2. Which language is widely used for data analysis?\nA)HTML    B) CSS   C) JAVA   D) PYHTONE ")
ans2 = st.text_input("Enter your choice...")
if ans2 == 'd' or ans=='D':
  score=5
else:
  score = 0 
st.write("Q3.What does SQL stand for?\nA)Simple Query Language   B) system Query language   C) structure Query lamguage   D) Sequential Query Language ")
ans3 = st.text_input("Enter your choice...")
if ans3 == 'c' or ans=='C':
  score=5
else:
  score = 0 
st.write("Q4.Which chart is best for showing trends over time?\nA)pie chat  B) line chat   C) bar chat   D) Scatter Plot ")
ans4 = st.text_input("Enter your choice...")
if ans4 == 'c' or ans=='C':
  score=5
else:
  score = 0      
if score == 20 :
  st.write("congratulations! you have scored",score,'in quiz')
  st.balloons()
elif score == 15 :
   st.write("congratulations! you have scored",score,'in quiz')
   st.snow() 
else:
  st.write("fail")
  
# n = st.checkbox("A")
# n = st.checkbox("B")
# n = st.text_input("Enter,,,,",placeholder="Please press enter to feed answer")
# st.write(n)

