from utils.login_manager import LoginManager
import streamlit as st
import pandas as pd

LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously

st.title('Kalorien Daten')

# Access the data from session state
data_df = st.session_state.get('data_df', None)
if data_df is None or data_df.empty:
    st.info('Keine Kalorien-Daten vorhanden. Erfassen Sie Ihre Daten auf der Startseite.')
    st.stop()

# Überprüfen, ob die Spalte 'timestamp' existiert und gültig ist
if 'timestamp' not in data_df.columns:
    st.error("Die Spalte 'timestamp' fehlt in den Daten. Bitte stellen Sie sicher, dass die Daten korrekt erfasst wurden.")
    st.stop()

# Konvertiere die 'timestamp'-Spalte in ein Datetime-Format, falls nötig
try:
    data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')
except Exception as e:
    st.error(f"Fehler beim Konvertieren der 'timestamp'-Spalte: {e}")
    st.stop()

# Entferne ungültige Datensätze mit fehlenden oder ungültigen Timestamps
if data_df['timestamp'].isnull().all():
    st.error("Alle Werte in der 'timestamp'-Spalte sind ungültig. Bitte überprüfen Sie die Daten.")
    st.stop()

data_df = data_df.dropna(subset=['timestamp'])

# Fehlende Spalten mit Standardwerten ergänzen
if 'calories' not in data_df.columns:
    st.warning("Die Spalte 'calories' fehlt in den Daten. Sie wird mit Standardwerten ergänzt.")
    data_df['calories'] = 0  # Standardwert hinzufügen

# Sort dataframe by timestamp
if not data_df.empty:
    data_df = data_df.sort_values('timestamp', ascending=False)
else:
    st.info("Keine gültigen Daten nach der Bereinigung vorhanden.")
    st.stop()

# Display table
st.dataframe(data_df)

# Optional: Add a plot for better visualization
st.subheader('Kalorienverbrauch über die Zeit')
if 'timestamp' in data_df.columns and 'calories' in data_df.columns:
    st.line_chart(data_df.set_index('timestamp')['calories'])
else:
    st.warning('Die Daten enthalten keine gültigen Spalten für die Grafik.')
# Display table
st.dataframe(data_df)

# Optional: Add a plot for better visualization
st.subheader('Kalorienverbrauch über die Zeit')
if 'timestamp' in data_df.columns and 'calories' in data_df.columns:
    st.line_chart(data_df.set_index('timestamp')['calories'])
else:
    st.warning('Die Daten enthalten keine gültigen Spalten für die Grafik.')