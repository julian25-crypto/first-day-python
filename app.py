import streamlit as st
import random

st.title("🎯 Simple Guessing Game")

# Initialize a secret number in session_state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)

if "message" not in st.session_state:
    st.session_state.message = ""

st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    if guess < st.session_state.secret:
        st.session_state.message = "Too low! 🔽"
    elif guess > st.session_state.secret:
        st.session_state.message = "Too high! 🔼"
    else:
        st.session_state.message = "🎉 Correct! You guessed it!"
        
    st.experimental_rerun()

st.write(st.session_state.message)

# Reset game
if st.button("New Game"):
    st.session_state.secret = random.randint(1, 100)
    st.session_state.message = ""
    st.experimental_rerun()
