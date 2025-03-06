import streamlit as st

def calculate_calories(age, weight, height, gender, activity_level):
    if gender == 'Male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    if activity_level == 'Sedentary':
        calories = bmr * 1.2
    elif activity_level == 'Lightly active':
        calories = bmr * 1.375
    elif activity_level == 'Moderately active':
        calories = bmr * 1.55
    elif activity_level == 'Very active':
        calories = bmr * 1.725
    else:
        calories = bmr * 1.9
    
    return calories

st.title('Kalorienrechner')

age = st.number_input('Alter', min_value=0, max_value=120, value=25)
weight = st.number_input('Gewicht (kg)', min_value=0.0, max_value=300.0, value=70.0)
height = st.number_input('Größe (cm)', min_value=0.0, max_value=250.0, value=175.0)
gender = st.selectbox('Geschlecht', ['Male', 'Female'])
activity_level = st.selectbox('Aktivitätslevel', ['Sedentary', 'Lightly active', 'Moderately active', 'Very active', 'Super active'])

if st.button('Kalorien berechnen'):
    calories = calculate_calories(age, weight, height, gender, activity_level)
    st.write(f'Der tägliche Kalorienbedarf beträgt: {calories:.2f} Kalorien')

