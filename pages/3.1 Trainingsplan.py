import streamlit as st

def generate_training_plan(goal, fitness_level, time_budget):
    # Dummy implementation of training plan generation
    plan = f"Training Plan for {goal} with fitness level {fitness_level} and time budget {time_budget} hours per week."
    return plan

def detailed_training_plan(goal, fitness_level, time_budget):
    days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    plan = {}
    
    for day in days:
        if goal == "5K":
            plan[day] = f"Laufen für {time_budget / 7:.2f} Stunden"
        elif goal == "10K":
            plan[day] = f"Laufen für {time_budget / 7:.2f} Stunden"
        elif goal == "Halbmarathon":
            plan[day] = f"Laufen für {time_budget / 7:.2f} Stunden"
        elif goal == "Marathon":
            plan[day] = f"Laufen für {time_budget / 7:.2f} Stunden"
    
    return plan

st.title("Trainingsplan-Generator")

st.header("Individueller Laufplan basierend auf Ihrem Ziel, Ihrer aktuellen Fitness und Ihrem Zeitbudget")

goal = st.selectbox("Wählen Sie Ihr Ziel", ["5K", "10K", "Halbmarathon", "Marathon"])
fitness_level = st.selectbox("Wählen Sie Ihr aktuelles Fitnesslevel", ["Anfänger", "Fortgeschritten", "Profi"])
time_budget = st.slider("Verfügbares Zeitbudget (Stunden pro Woche)", 1, 20, 5)

if st.button("Trainingsplan erstellen"):
    plan = generate_training_plan(goal, fitness_level, time_budget)
    st.write(plan)

if st.button("Detaillierten Trainingsplan erstellen"):
    detailed_plan = detailed_training_plan(goal, fitness_level, time_budget)
    for day, activity in detailed_plan.items():
        st.write(f"{day}: {activity}")