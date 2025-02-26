import streamlit as st

def get_fitness_exercises(goal, fitness_level):
    exercises = {
        "Anfänger": ["Liegestütze", "Kniebeugen", "Plank", "Lunges"],
        "Fortgeschritten": ["Burpees", "Klimmzüge", "Mountain Climbers", "Russian Twists"],
        "Profi": ["Handstand Push-Ups", "Pistol Squats", "Muscle-Ups", "Dragon Flags"]
    }
    
    return exercises.get(fitness_level, [])

st.title("Fitness-Übungen")

st.header("Individuelle Fitness-Übungen basierend auf Ihrem Ziel und Fitnesslevel")

goal = st.selectbox("Wählen Sie Ihr Ziel", ["Kraftaufbau", "Ausdauer", "Flexibilität", "Gewichtsverlust"])
fitness_level = st.selectbox("Wählen Sie Ihr aktuelles Fitnesslevel", ["Anfänger", "Fortgeschritten", "Profi"])

if st.button("Übungen anzeigen"):
    exercises = get_fitness_exercises(goal, fitness_level)
    if exercises:
        st.write(f"Empfohlene Übungen für {fitness_level}:")
        for exercise in exercises:
            st.write(f"- {exercise}")
    else:
        st.write("Keine Übungen gefunden für das ausgewählte Fitnesslevel.")