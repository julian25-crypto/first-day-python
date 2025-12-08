import streamlit as st

st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter 1st number", value=0)
num2 = st.number_input("Enter 2nd number", value=0)

# Perform operations when button is clicked
if st.button("Calculate"):
    st.write("### Results:")
    st.write(f"**Addition:** {num1 + num2}")
    st.write(f"**Subtraction:** {num1 - num2}")
    st.write(f"**Multiplication:** {num1 * num2}")
    
    if num2 != 0:
        st.write(f"**Division:** {num1 / num2}")
    else:
        st.write("**Division:** Cannot divide by zero")
