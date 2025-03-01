import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Dictionary of countries and their landmarks
# Dictionary of countries and their landmarks with coordinates
landmarks = {
    "Deutschland": [
        {"name": "Brandenburger Tor", "lat": 52.516275, "lon": 13.377704},
        {"name": "Kölner Dom", "lat": 50.941278, "lon": 6.958281},
        {"name": "Neuschwanstein", "lat": 47.557574, "lon": 10.749800}
    ],
    "Frankreich": [
        {"name": "Eiffelturm", "lat": 48.858844, "lon": 2.294351},
        {"name": "Louvre", "lat": 48.860611, "lon": 2.337644},
        {"name": "Notre-Dame", "lat": 48.852968, "lon": 2.349902}
    ],
    "Italien": [
        {"name": "Kolosseum", "lat": 41.890210, "lon": 12.492231},
        {"name": "Schiefer Turm von Pisa", "lat": 43.722952, "lon": 10.396597},
        {"name": "Venedig", "lat": 45.440847, "lon": 12.315515}
    ],
    "Spanien": [
        {"name": "Sagrada Familia", "lat": 41.403629, "lon": 2.174356},
        {"name": "Alhambra", "lat": 37.176077, "lon": -3.588141},
        {"name": "Park Güell", "lat": 41.414494, "lon": 2.152694}
    ],
    "USA": [
        {"name": "Freiheitsstatue", "lat": 40.689247, "lon": -74.044502},
        {"name": "Grand Canyon", "lat": 36.106965, "lon": -112.112997},
        {"name": "Golden Gate Bridge", "lat": 37.819929, "lon": -122.478255}
    ]
}

# Streamlit app
st.title("Sehenswürdigkeiten Finder")

# User input for country
country = st.text_input("Geben Sie ein Land ein:")

# Display landmarks if country is in the dictionary
if country:
    if country in landmarks:
        st.write(f"Sehenswürdigkeiten in {country}:")
        # Create a map centered around the first landmark
        m = folium.Map(location=[landmarks[country][0]["lat"], landmarks[country][0]["lon"]], zoom_start=5)
        for landmark in landmarks[country]:
            st.write(f"- {landmark['name']}")
            # Add marker to the map
            folium.Marker(
                location=[landmark["lat"], landmark["lon"]],
                popup=landmark["name"]
            ).add_to(m)
        # Display the map
        st_folium(m, width=700, height=500)
    else:
        st.write("Land nicht gefunden. Bitte versuchen Sie es erneut.")

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