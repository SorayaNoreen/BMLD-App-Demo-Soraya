from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 

import streamlit as st
from datetime import datetime
from utils.data_manager import DataManager

def berechne_kalorien(alter, gewicht, groesse, geschlecht, aktivitaetslevel):
    # Berechnung des Grundumsatzes (BMR) basierend auf Geschlecht
    if geschlecht == 'Männlich':
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * groesse) - (5.677 * alter)
    else:
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * groesse) - (4.330 * alter)
    
    # Anpassung des BMR basierend auf dem Aktivitätslevel
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

# Titel der Streamlit-App
st.title('Kalorienrechner')

# Eingabefelder für die Benutzer
alter = st.number_input('Alter', min_value=0, max_value=120, value=25)
gewicht = st.number_input('Gewicht (kg)', min_value=0.0, max_value=300.0, value=70.0)
groesse = st.number_input('Größe (cm)', min_value=0.0, max_value=250.0, value=175.0)
geschlecht = st.selectbox('Geschlecht', ['Männlich', 'Weiblich', 'Divers'])
aktivitaetslevel = st.selectbox('Aktivitätslevel', ['Wenig aktiv', 'Leicht aktiv', 'Mäßig aktiv', 'Sehr aktiv', 'Extrem aktiv'])

# Button zur Berechnung der Kalorien
if st.button('Kalorien berechnen'):
    # Berechnung des Kalorienbedarfs
    kalorien = berechne_kalorien(alter, gewicht, groesse, geschlecht, aktivitaetslevel)
    st.write(f'Der tägliche Kalorienbedarf beträgt: {kalorien:.2f} Kalorien')
    
    # Aktuelles Datum und Uhrzeit
    jetzt = datetime.now()
    st.write(f'Berechnet am: {jetzt.strftime("%d.%m.%Y %H:%M:%S")}')
    
    # Daten in ein Dictionary speichern
    result = {
        'Alter': alter,
        'Gewicht': gewicht,
        'Größe': groesse,
        'Geschlecht': geschlecht,
        'Aktivitätslevel': aktivitaetslevel,
        'Kalorienbedarf': kalorien,
        'Berechnet am': jetzt.strftime("%d.%m.%Y %H:%M:%S")
    }
    
    # Speichern der Daten mit DataManager
    DataManager().append_record(session_state_key='data_df', record_dict=result)
    st.success("Die Daten wurden erfolgreich gespeichert!")