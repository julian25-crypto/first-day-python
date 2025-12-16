import streamlit as st

# Initialize an empty dictionary to store bookings
bookings = {}

# App title
st.title("Movie Ticket Booking")

# Input fields for movie and seat
movie_to_watch = st.text_input("Which movie do you want to watch?")
seat = st.text_input("Which seat do you prefer?")

# Logic to book the ticket
if movie_to_watch and seat:
    booking_key = movie_to_watch + "-" + seat
    
    # Show the booking details
    if booking_key not in bookings:
        bookings[booking_key] = "BOOKED"
        st.success(f"Booking successful for '{movie_to_watch}' at seat '{seat}'")
    else:
        st.warning(f"Seat '{seat}' for movie '{movie_to_watch}' is already booked!")
    
    # Display all bookings
    st.write("Current Bookings:", bookings)
