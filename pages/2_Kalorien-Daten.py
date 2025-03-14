from utils.login_manager import LoginManager
import streamlit as st

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

# Überprüfen, ob die Spalte 'timestamp' existiert
if 'timestamp' not in data_df.columns:
    st.error("Die Spalte 'timestamp' fehlt in den Daten. Bitte stellen Sie sicher, dass die Daten korrekt erfasst wurden.")
    st.stop()

# Konvertiere die 'timestamp'-Spalte in ein Datetime-Format, falls nötig
if not pd.api.types.is_datetime64_any_dtype(data_df['timestamp']):
    data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')

# Entferne ungültige Datensätze mit fehlenden oder ungültigen Timestamps
data_df = data_df.dropna(subset=['timestamp'])

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)

# Optional: Add a plot for better visualization
st.subheader('Kalorienverbrauch über die Zeit')
if 'timestamp' in data_df.columns and 'calories' in data_df.columns:
    st.line_chart(data_df.set_index('timestamp')['calories'])
else:
    st.warning('Die Daten enthalten keine gültigen Spalten für die Grafik.')