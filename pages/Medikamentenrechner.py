import streamlit as st

st.title("Medikamentenrechner")

def calculate_dosage(weight, medication):
    if medication == "Ibuprofen":
        return weight * 10  # mg per kg
    elif medication == "Paracetamol":
        return weight * 15  # mg per kg
    elif medication == "NSAR":
        return weight * 12  # mg per kg
    else:
        return 0

st.header("Dosierungsrechner")

weight = st.number_input("Geben Sie das Gewicht des Patienten in kg ein:", min_value=0.0, step=0.1)
medication = st.selectbox("Wählen Sie das Medikament aus:", ["Ibuprofen", "Paracetamol", "NSAR"])

if st.button("Berechne Dosierung"):
    dosage = calculate_dosage(weight, medication)
    st.write(f"Die empfohlene Dosierung für {medication} beträgt {dosage} mg.")