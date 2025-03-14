from utils.login_manager import LoginManager
import streamlit as st

# ====== Start Login Block ======
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === Kalorien Grafik ===

st.title('Kalorien Grafik')

# Zugriff auf die gespeicherten Daten im Session State
data_df = st.session_state.get('data_df', None)

# Überprüfen, ob Daten vorhanden sind
if data_df is None or data_df.empty:
    st.info('Keine Kalorien-Daten vorhanden. Erfassen Sie Ihre Kalorien auf der Startseite.')
    st.stop()

# Überprüfen, ob die notwendigen Spalten existieren
required_columns = ['timestamp', 'calories_burned', 'calories_intake']
missing_columns = [col for col in required_columns if col not in data_df.columns]

if missing_columns:
    st.error(f"Die folgenden Spalten fehlen in den Daten: {', '.join(missing_columns)}")
    st.stop()

# Konvertiere die 'timestamp'-Spalte in ein Datetime-Format, falls nötig
if not pd.api.types.is_datetime64_any_dtype(data_df['timestamp']):
    data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')

# Entferne ungültige Datensätze mit fehlenden oder ungültigen Timestamps
data_df = data_df.dropna(subset=['timestamp'])

# Kalorienverbrauch über Zeit
st.line_chart(data=data_df.set_index('timestamp')['calories_burned'], 
              use_container_width=True)
st.caption('Kalorienverbrauch über Zeit (kcal)')

# Kalorienaufnahme über Zeit
st.line_chart(data=data_df.set_index('timestamp')['calories_intake'], 
              use_container_width=True)
st.caption('Kalorienaufnahme über Zeit (kcal)')

# Kalorienbilanz über Zeit
data_df['calorie_balance'] = data_df['calories_intake'] - data_df['calories_burned']
st.line_chart(data=data_df.set_index('timestamp')['calorie_balance'], 
              use_container_width=True)
st.caption('Kalorienbilanz über Zeit (kcal)')