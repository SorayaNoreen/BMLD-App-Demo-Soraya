import streamlit as st

# Funktion zur Berechnung der Stoffmenge
def berechne_stoffmenge(masse, molare_masse):
    return masse / molare_masse

# Streamlit App
st.title("Stoffmengenrechner")

st.write("Geben Sie die Masse und die molare Masse des Elements ein, um die Stoffmenge zu berechnen.")

masse = st.number_input("Masse (in Gramm):", min_value=0.0, format="%.2f")
molare_masse = st.number_input("Molare Masse (in g/mol):", min_value=0.0, format="%.2f")

if st.button("Berechnen"):
    if molare_masse > 0:
        stoffmenge = berechne_stoffmenge(masse, molare_masse)
        st.success(f"Die Stoffmenge beträgt {stoffmenge:.4f} mol")
    else:
        st.error("Die molare Masse muss größer als 0 sein.")