import streamlit as st

st.title("🎵 WELCOME TO Trisha's Playlist")
st.write("=" * 20)

# Initial playlist
liked_songs = [
    "night changes",
    "what makes you beautiful",
    "baby",
    "belong together",
    "all around the world"
]

st.subheader("Original Playlist")
st.write(liked_songs)
st.write("=" * 80)

# Add first song
add_item = "strong"
liked_songs.append(add_item)

st.subheader("After Adding 'strong'")
st.write(liked_songs)
st.write("=" * 100)

# Add second song
add_item = "perfect"
liked_songs.append(add_item)

st.subheader("After Adding 'perfect'")
st.write(liked_songs)
st.write("=" * 115)

# Remove a song
remove_item = "baby"
liked_songs.remove(remove_item)

st.subheader("After Removing 'baby'")
st.write(liked_songs)
st.write("=" * 110)

