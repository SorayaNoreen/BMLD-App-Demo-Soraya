import streamlit as st


# BMI Berechner
st.header("BMI Berechner")

# Eingabe des Gewichts
gewicht = st.number_input("Geben Sie Ihr Gewicht in Kilogramm ein:", min_value=0.0, step=0.1)

# Eingabe der Größe
groesse = st.number_input("Geben Sie Ihre Größe in Metern ein:", min_value=0.0, step=0.01)

# Berechnung des BMI
if gewicht > 0 and groesse > 0:
    bmi = gewicht / (groesse ** 2)
    st.write(f"Ihr BMI beträgt: {bmi:.2f}")
else:
    st.write("Bitte geben Sie gültige Werte für Gewicht und Größe ein.")

    # Einfügen eines Logos
    st.image("https://example.com/path-to-your-logo.png", caption="BMI Berechner Logo")