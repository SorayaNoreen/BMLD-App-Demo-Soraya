import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

st.title("BMI Rechner")

weight = st.number_input("Gewicht (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Größe (m)", min_value=0.0, format="%.2f")

if st.button("Berechne BMI"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Ihr BMI ist: {bmi:.2f}")
    else:
        st.write("Bitte geben Sie eine gültige Größe ein.")