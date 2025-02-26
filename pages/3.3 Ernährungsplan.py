import streamlit as st

def generate_nutrition_plan(goal, dietary_preferences):
    # Dummy implementation of nutrition plan generation
    plan = f"Ernährungsplan für {goal} mit den Präferenzen {dietary_preferences}."
    return plan

st.title("Ernährungsplan-Generator")

st.header("Individueller Ernährungsplan basierend auf Ihrem Ziel und Ihren Ernährungspräferenzen")

goal = st.selectbox("Wählen Sie Ihr Ziel", ["Gewichtsverlust", "Muskelaufbau", "Gesundheitserhaltung"])
dietary_preferences = st.selectbox("Wählen Sie Ihre Ernährungspräferenzen", ["Vegetarisch", "Vegan", "Keto", "Paleo", "Keine Präferenzen"])

if st.button("Ernährungsplan erstellen"):
    plan = generate_nutrition_plan(goal, dietary_preferences)
    st.write(plan)