from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 

import streamlit as st
from datetime import datetime
from utils.data_manager import DataManager
from functions.Berechner import berechne_kalorien

# Titel der Streamlit-App
st.title('Kalorienrechner')

# Eingabefelder für die Benutzer
alter = st.number_input('Alter', min_value=0, max_value=120, value=25)
gewicht = st.number_input('Gewicht (kg)', min_value=0.0, max_value=300.0, value=70.0)
groesse = st.number_input('Größe (cm)', min_value=0.0, max_value=250.0, value=175.0)
geschlecht = st.selectbox('Geschlecht', ['Männlich', 'Weiblich', 'Divers'])
aktivitaetslevel = st.selectbox('Aktivitätslevel', ['Wenig aktiv', 'Leicht aktiv', 'Mäßig aktiv', 'Sehr aktiv', 'Extrem aktiv'])

if st.button('Kalorien berechnen'):
    # Berechnung des Kalorienbedarfs
    kalorien = berechne_kalorien(alter, gewicht, groesse, geschlecht, aktivitaetslevel)
    st.write(f'Der tägliche Kalorienbedarf beträgt: {kalorien:.2f} Kalorien')
    
    # Aktuelles Datum und Uhrzeit
    jetzt = datetime.now()
    st.write(f'Berechnet am: {jetzt.strftime("%d.%m.%Y %H:%M:%S")}')
    
    # Beispielwerte für Kalorienverbrauch und Kalorienaufnahme
    Kalorien_verbrannt = kalorien * 0.8  # Beispiel: 80% des Kalorienbedarfs
    Kalorien_Aufnahme = kalorien * 1.2  # Beispiel: 120% des Kalorienbedarfs

    # Daten in ein Dictionary speichern
    result = {
        'timestamp': jetzt.strftime("%Y-%m-%d %H:%M:%S"),
        'Alter': alter,
        'Gewicht': gewicht,
        'Größe': groesse,
        'Geschlecht': geschlecht,
        'Aktivitätslevel': aktivitaetslevel,
        'Kalorienbedarf': kalorien,
        'Kalorien': kalorien,  # Hier war der Fehler: Doppelpunkt fehlte
        'Kalorien_verbrannt': Kalorien_verbrannt,
        'Kalorien_Aufnahme': Kalorien_Aufnahme
    }

    # Speichern der Daten mit DataManager
    DataManager().append_record(session_state_key='data_df', record_dict=result)
    st.success("Die Daten wurden erfolgreich gespeichert!")

    # Speichern der Daten mit DataManager
    DataManager().append_record(session_state_key='data_df', record_dict=result)
    st.success("Die Daten wurden erfolgreich gespeichert!")