import streamlit as st

st.write("Hello welcome to Quiz Game application he")
st.sidebar.markdown("Quiz Menu...")
st.sidebar.markdown("Quiz Game")
score = 0
st.write("Q1. Which is the first alphabet of english language?\nA) c   B) d    C) a   D) f")
ans = st.text_input("Enter your choice...",placeholder="Please press enter to feed answer")
if ans == 'c' or ans=='C':
  score=5
else:
  score = 0
if score == 5 :
  st.write("congratulations! you have scored",score,'in quiz')
  st.balloons()
# n = st.checkbox("A")
# n = st.checkbox("B")
# n = st.text_input("Enter,,,,",placeholder="Please press enter to feed answer")
# st.write(n)

