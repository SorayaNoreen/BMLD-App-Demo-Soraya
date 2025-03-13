import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title("Kalorienrechner")

st.write("Ein Kalorienrechner bestimmt, wie viele Kalorien du täglich brauchst, basierend auf Faktoren wie Alter, Geschlecht, Größe, Gewicht und Aktivitätslevel. Er hilft dir, deinen Grundumsatz (Kalorienverbrauch im Ruhezustand) und Gesamtumsatz (inklusive Bewegung) zu berechnen. So kannst du dein Kalorienziel festlegen – ob zum Halten, Abnehmen oder Zunehmen.") 
st.write("🍎🥗🍔🍕")


st.write("Diese App wurde von Soraya Gfrerer entwickelt.")
st.write("E-Mail Adresse: gfrersor@students.zhaw.ch")  
