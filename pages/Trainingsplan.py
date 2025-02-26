import streamlit as st

def generate_training_plan(goal, fitness_level, time_budget):
    # Dummy implementation of training plan generation
    plan = f"Training Plan for {goal} with fitness level {fitness_level} and time budget {time_budget} hours per week."
    return plan

st.title("Trainingsplan-Generator")

st.header("Individueller Laufplan basierend auf Ihrem Ziel, Ihrer aktuellen Fitness und Ihrem Zeitbudget")

goal = st.selectbox("Wählen Sie Ihr Ziel", ["5K", "10K", "Halbmarathon", "Marathon"])
fitness_level = st.selectbox("Wählen Sie Ihr aktuelles Fitnesslevel", ["Anfänger", "Fortgeschritten", "Profi"])
time_budget = st.slider("Verfügbares Zeitbudget (Stunden pro Woche)", 1, 20, 5)

if st.button("Trainingsplan erstellen"):
    plan = generate_training_plan(goal, fitness_level, time_budget)
    st.write(plan)