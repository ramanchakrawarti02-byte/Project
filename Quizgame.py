import streamlit as st
st.write('Hello Students!')
st.write
Score= 0
st.write("Welcome to quiz game....")
st.write('Q1. What is the first alphabetb of english language?\nA)C B)T\n C)A  D)F')
ans = st.text_input("Enter your choice....")
if ans.lower()== 'c':
    Score +=5
st.write('_________________________')

st.write('Q2. What is the National Bird?\n A)Peacock  B)Crow\n  C)pegion  D)Duck')
ans = st.text_input ("Enter Your Choice....")

if ans.lower() == 'a':
    Score +=5
st.write('----------------------------------------------------------------------------------')
st.write("Q3. what is the national Animal?\n A) tiger B) lion  C) Elephant D) bear")
ans= st.text_input("enter ur chioce....")
if ans.lower() == 'a':
     Score +=5
st.write('----------------------------------------------------------------------------')
st.write('Q4. what is middle alphabet in CAT?\n A) T   B) C   C)W    D)A')
ans = st.text_input("Enter ur choice....")
if ans.lower() == 'd':
   Score+=5
st.write('--------------------------------------------------------------------------')
st.write ('What is the national vegetable?\n A)tomato B) onion  C) peas  D) brinjal')
ans = st.text_input("Enter ur choice.....")
if ans.lower() == 'd':
     Score+=5
st.write ('---------------------------------------------------------------------')
if Score == 25:
    st.write("Congratulation !! you have scored__",Score,"1st position")
    st.balloons()

elif Score == 15:
    st.write("Congratulation !! you have scored__",Score,"2nd position")
    st.snow()

else:
    st.write("Congratulation !! you have scored__",Score,"better Luck next time")
