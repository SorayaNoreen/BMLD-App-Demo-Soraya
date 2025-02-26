import streamlit as st

def calculate_dosage(weight, medication):
    if medication == "Ibuprofen":
        # Dosage: 10 mg/kg every 6-8 hours, max 40 mg/kg/day
        dose = weight * 10
        max_dose = weight * 40
    elif medication == "Paracetamol":
        # Dosage: 15 mg/kg every 4-6 hours, max 60 mg/kg/day
        dose = weight * 15
        max_dose = weight * 60
    else:
        dose = 0
        max_dose = 0
    return dose, max_dose

st.title("Medikamentenrechner")

weight = st.number_input("Geben Sie das Gewicht des Patienten in kg ein:", min_value=0.0, step=0.1)
medication = st.selectbox("Wählen Sie das Medikament:", ["Ibuprofen", "Paracetamol"])

if st.button("Berechnen"):
    dose, max_dose = calculate_dosage(weight, medication)
    st.write(f"Empfohlene Einzeldosis für {medication}: {dose} mg")
    st.write(f"Maximale Tagesdosis für {medication}: {max_dose} mg")