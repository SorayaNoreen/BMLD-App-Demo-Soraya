import streamlit as st

st.title("Verdünnungsrechner")



def calculate_dilution(c1, v1, c2):
    return (c1 * v1) / c2

st.header("Berechnung der Verdünnung")

c1 = st.number_input("Konzentration der Stammlösung (C1) in mol/L", min_value=0.0, step=0.01)
v1 = st.number_input("Volumen der Stammlösung (V1) in L", min_value=0.0, step=0.01)
c2 = st.number_input("Gewünschte Endkonzentration (C2) in mol/L", min_value=0.0, step=0.01)

if st.button("Berechnen"):
    if c2 != 0:
        v2 = calculate_dilution(c1, v1, c2)
        st.success(f"Das benötigte Endvolumen (V2) ist {v2:.2f} L")
    else:
        st.error("Die Endkonzentration (C2) darf nicht 0 sein.")