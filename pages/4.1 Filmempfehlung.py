import streamlit as st

# Dictionary of genres and their movie recommendations
movies = {
    "Action": ["Mad Max: Fury Road", "Die Hard", "John Wick", "The Dark Knight", "Gladiator", "Kill Bill", "Speed", "The Raid", "The Terminator", "The Bourne Identity", "Lethal Weapon"],
    "Abenteuer": ["Indiana Jones", "The Lord of the Rings", "Pirates of the Caribbean", "Jurassic Park", "The Hobbit", "Avatar", "The Revenant", "Life of Pi", "The Jungle Book", "Jumanji"],
    "Komödie": ["Superbad", "Step Brothers", "The Hangover", "Anchorman", "Dumb and Dumber", "Bridesmaids", "Groundhog Day", "Ferris Bueller's Day Off", "The Big Lebowski", "Shaun of the Dead"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather", "Schindler's List", "Fight Club", "The Social Network", "A Beautiful Mind", "The Pursuit of Happyness", "Good Will Hunting", "12 Years a Slave"],
    "Thriller": ["Se7en (1995)", "The Silence of the Lambs (1991)", "Gone Girl (2014)", "Prisoners (2013)", "Zodiac (2007)", "No Country for Old Men (2007)", "The Girl with the Dragon Tattoo (2011)", "Black Swan (2010)", "Oldboy (2003)", "Mystic River (2003)"],
    "Horror": ["The Conjuring", "Get Out", "A Nightmare on Elm Street", "The Exorcist", "Hereditary", "It", "The Shining", "Halloween", "The Babadook", "Paranormal Activity"],
    "Science Fiction": ["Inception", "The Matrix", "Blade Runner 2049", "Interstellar", "Star Wars", "The Fifth Element", "E.T. the Extra-Terrestrial", "Back to the Future", "The Terminator", "Minority Report"],
    "Fantasy": ["The Lord of the Rings: The Fellowship of the Ring (2001)", "Harry Potter and the Sorcerer's Stone (2001)", "Pan's Labyrinth (2006)", "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe (2005)", "The Shape of Water (2017)", "Stardust (2007)", "Spirited Away (2001)", "Alice in Wonderland (2010)", "The Wizard of Oz (1939)", "Fantastic Beasts and Where to Find Them (2016)"],
    "Krimi": ["The Godfather (1972)", "Goodfellas (1990)", "The Departed (2006)", "Heat (1995)", "L.A. Confidential (1997)", "Pulp Fiction (1994)", "Chinatown (1974)", "Snatch (2000)", "American Gangster (2007)", "The Irishman (2019)"],
    "Mystery": ["Shutter Island (2010)", "The Sixth Sense (1999)", "Memento (2000)", "The Prestige (2006)", "Donnie Darko (2001)", "Knives Out (2019)", "Mulholland Drive (2001)", "The Others (2001)", "Clue (1985)", "The Da Vinci Code (2006)"],
    "Western": ["The Good, the Bad and the Ugly (1966)", "Django Unchained (2012)", "True Grit (2010)", "The Magnificent Seven (1960)", "Once Upon a Time in the West (1968)", "3:10 to Yuma (2007)", "No Country for Old Men (2007)", "The Hateful Eight (2015)", "Unforgiven (1992)", "Tombstone (1993)"],
    "Romanze": ["Titanic (1997)", "The Notebook (2004)", "La La Land (2016)", "Pretty Woman (1990)", "Pride and Prejudice (2005)", "Call Me by Your Name (2017)", "Brokeback Mountain (2005)", "Eternal Sunshine of the Spotless Mind (2004)", "10 Things I Hate About You (1999)", "Before Sunrise (1995)"],
    "Musical": ["The Greatest Showman (2017)", "Les Misérables (2012)", "Moulin Rouge! (2001)", "West Side Story (1961)", "Grease (1978)", "Chicago (2002)", "La La Land (2016)", "The Sound of Music (1965)", "Sweeney Todd: The Demon Barber of Fleet Street (2007)", "Singing in the Rain (1952)"],
    "Dokumentation": ["Planet Earth (2006)", "Free Solo (2018)", "The Social Dilemma (2020)", "Won't You Be My Neighbor? (2018)", "13th (2016)", "Blackfish (2013)", "Making a Murderer (2015)", "Bowling for Columbine (2002)", "Searching for Sugar Man (2012)", "The Act of Killing (2012)"]
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