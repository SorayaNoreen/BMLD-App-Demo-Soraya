import streamlit as st

# Dictionary of genres and their movie recommendations
movies = {
    "Action": ["Mad Max: Fury Road", "Die Hard", "John Wick"],
    "Komödie": ["Superbad", "Step Brothers", "The Hangover"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "Horror": ["The Conjuring", "Get Out", "A Nightmare on Elm Street"],
    "Science Fiction": ["Inception", "The Matrix", "Blade Runner 2049"]
}

# Streamlit app
st.title("Filmempfehlungen")

# User input for genre
genre = st.selectbox("Wählen Sie ein Genre", list(movies.keys()))

# Display movie recommendations if genre is selected
if genre:
    st.write(f"Empfohlene Filme im Genre {genre}:")
    for movie in movies[genre]:
        st.write(f"- {movie}")