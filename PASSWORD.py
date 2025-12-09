import streamlit as st

st.title("Attendance Slot Creator")

# Inputs
division = st.text_input("Enter Division")
professor = st.text_input("Enter Faculty/Professor Name")
subject = st.text_input("Enter Subject")
password_by_teacher = 12345  # Fixed teacher password

password_by_student = st.number_input("Enter Student Password", step=1)

# Button
if st.button("Submit Attendance"):
    st.write("### Attendance Slot Created For:")
    st.write(f"**Division:** {division}")
    st.write(f"**Professor:** {professor}")
    st.write(f"**Subject:** {subject}")

    # Password check
    if password_by_student == password_by_teacher:
        st.success("Attendance Given ✅")
    else:
        st.error("Attendance NOT Given ❌")




