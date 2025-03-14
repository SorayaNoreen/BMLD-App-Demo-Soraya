import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="LN1_Demo_App")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

import streamlit as st

st.title("Kalorienrechner")

st.write("Ein Kalorienrechner bestimmt, wie viele Kalorien du täglich brauchst, basierend auf Faktoren wie Alter, Geschlecht, Größe, Gewicht und Aktivitätslevel. Er hilft dir, deinen Grundumsatz (Kalorienverbrauch im Ruhezustand) und Gesamtumsatz (inklusive Bewegung) zu berechnen. So kannst du dein Kalorienziel festlegen – ob zum Halten, Abnehmen oder Zunehmen.") 
st.write("🍎🥗🍔🍕")


st.write("Diese App wurde von Soraya Gfrerer entwickelt.")
st.write("E-Mail Adresse: gfrersor@students.zhaw.ch")  
