from utils.login_manager import LoginManager
import streamlit as st

# ====== Start Login Block ======
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === Kalorien Grafik ===

st.title('Kalorien Verlauf')

# Zugriff auf die gespeicherten Daten im Session State
data_df = st.session_state.get('data_df', None)
if data_df is None or data_df.empty:
    st.info('Keine Kalorien-Daten vorhanden. Erfassen Sie Ihre Kalorien auf der Startseite.')
    st.stop()

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