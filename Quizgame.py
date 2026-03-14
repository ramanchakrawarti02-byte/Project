import streamlit as st

st.write("Hello Students!")
score = 0
st.write("Welcome to quiz game....")

# Q1
st.write("Q1. What is the first alphabetb of english language?\nA)C B)T\n C)A  D)F")
    
ans1 = st.text_input("Enter answer for Q1")

# Q2
st.write("Q2 What is the National Bird?\n A)Peacock  B)Crow\n  C)pegion  D)Duck")
ans2 = st.text_input("Enter answer for Q2")

# Q3
st.write("Q3. what is the national Animal?\n A) tiger B) lion  C) Elephant D) bear")
ans3 = st.text_input("Enter answer for Q3")

# Q4
st.write("Q4. what is middle alphabet in CAT?\n A) T   B) C   C)W    D)A")
ans4 = st.text_input("Enter answer for Q4")

# Q5
st.write("Q5.What is the national vegetable?\n A)tomato B) onion  C) peas  D) brinjal")
ans5 = st.text_input("Enter answer for Q5")

# Submit button
if st.button("Submit Quiz"):

    score = 0

    if ans1.lower() == "c":
        score += 5
    if ans2.lower() == "a":
        score += 5
    if ans3.lower() == "a":
        score += 5
    if ans4.lower() == "d":
        score += 5
    if ans5.lower() == "d":
        score += 5

    if score == 25:
        st.write("Congratulations! You scored", score, "1st Position")
        st.balloons()
    elif score >= 15:
        st.write("Congratulations! You scored", score, "2nd Position")
        st.snow()
    else:
        st.write("You scored", score, "Better luck next time")
