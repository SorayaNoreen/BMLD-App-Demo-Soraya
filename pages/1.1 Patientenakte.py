import streamlit as st

# Initialize session state if not already done
if 'patient_data' not in st.session_state:
    st.session_state.patient_data = {
        'weight': [],
        'height': [],
        'blood_pressure': []
    }

# Title of the app
st.title("Digitale Patientenakte")

# Input field for date
date = st.date_input("Datum")

# Button to add the data to the patient record
if st.button("Daten hinzufügen"):
    st.session_state.patient_data['weight'].append(weight)
    st.session_state.patient_data['height'].append(height)
    st.session_state.patient_data['blood_pressure'].append((systolic_bp, diastolic_bp))
    st.session_state.patient_data.setdefault('date', []).append(date)
    st.success("Daten erfolgreich hinzugefügt!")

# Display the patient data
st.subheader("Patientendaten")
st.write("Datum:", st.session_state.patient_data.get('date', []))
st.write("Gewicht (kg):", st.session_state.patient_data['weight'])
st.write("Länge (cm):", st.session_state.patient_data['height'])
st.write("Blutdruck (mmHg):", st.session_state.patient_data['blood_pressure'])

# Input fields for weight, height, and blood pressure
weight = st.number_input("Gewicht (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Länge (cm)", min_value=0.0, format="%.2f")
systolic_bp = st.number_input("Systolischer Blutdruck (mmHg)", min_value=0)
diastolic_bp = st.number_input("Diastolischer Blutdruck (mmHg)", min_value=0)

# Button to add the data to the patient record
if st.button("Daten hinzufügen"):
    st.session_state.patient_data['weight'].append(weight)
    st.session_state.patient_data['height'].append(height)
    st.session_state.patient_data['blood_pressure'].append((systolic_bp, diastolic_bp))
    st.success("Daten erfolgreich hinzugefügt!")

# Display the patient data
st.subheader("Patientendaten")
st.write("Gewicht (kg):", st.session_state.patient_data['weight'])
st.write("Länge (cm):", st.session_state.patient_data['height'])
st.write("Blutdruck (mmHg):", st.session_state.patient_data['blood_pressure'])
