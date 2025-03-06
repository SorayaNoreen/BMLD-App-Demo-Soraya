import streamlit as st
from datetime import datetime

def berechne_kalorien(alter, gewicht, groesse, geschlecht, aktivitaetslevel):
    if geschlecht == 'Männlich':
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * groesse) - (5.677 * alter)
    else:
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * groesse) - (4.330 * alter)
    
    if aktivitaetslevel == 'Wenig aktiv':
        kalorien = bmr * 1.2
    elif aktivitaetslevel == 'Leicht aktiv':
        kalorien = bmr * 1.375
    elif aktivitaetslevel == 'Mäßig aktiv':
        kalorien = bmr * 1.55
    elif aktivitaetslevel == 'Sehr aktiv':
        kalorien = bmr * 1.725
    else:
        kalorien = bmr * 1.9
    
    return kalorien

st.title('Kalorienrechner')

alter = st.number_input('Alter', min_value=0, max_value=120, value=25)
gewicht = st.number_input('Gewicht (kg)', min_value=0.0, max_value=300.0, value=70.0)
groesse = st.number_input('Größe (cm)', min_value=0.0, max_value=250.0, value=175.0)
geschlecht = st.selectbox('Geschlecht', ['Männlich', 'Weiblich'])
aktivitaetslevel = st.selectbox('Aktivitätslevel', ['Wenig aktiv', 'Leicht aktiv', 'Mäßig aktiv', 'Sehr aktiv', 'Extrem aktiv'])

if st.button('Kalorien berechnen'):
    kalorien = berechne_kalorien(alter, gewicht, groesse, geschlecht, aktivitaetslevel)
    st.write(f'Der tägliche Kalorienbedarf beträgt: {kalorien:.2f} Kalorien')
    jetzt = datetime.now()
    st.write(f'Berechnet am: {jetzt.strftime("%d.%m.%Y %H:%M:%S")}')