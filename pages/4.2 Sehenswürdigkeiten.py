import streamlit as st

# Dictionary of countries and their landmarks
landmarks = {
    "Deutschland": ["Brandenburger Tor", "Kölner Dom", "Neuschwanstein"],
    "Frankreich": ["Eiffelturm", "Louvre", "Notre-Dame"],
    "Italien": ["Kolosseum", "Schiefer Turm von Pisa", "Venedig"],
    "Spanien": ["Sagrada Familia", "Alhambra", "Park Güell"],
    "USA": ["Freiheitsstatue", "Grand Canyon", "Golden Gate Bridge"]
}

# Streamlit app
st.title("Sehenswürdigkeiten Finder")

# User input for country
country = st.text_input("Geben Sie ein Land ein:")

# Display landmarks if country is in the dictionary
if country:
    if country in landmarks:
        st.write(f"Sehenswürdigkeiten in {country}:")
        for landmark in landmarks[country]:
            st.write(f"- {landmark}")
    else:
        st.write("Land nicht gefunden. Bitte versuchen Sie es erneut.")