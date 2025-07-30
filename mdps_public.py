# -*- coding: utf-8 -*-
"""
Multiple Disease Prediction System
Created on Wed Jul 30, 2025
@author: jainv
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ====================================================
# Load Pre-trained Machine Learning Models (saved using pickle)
# ====================================================
# NOTE: Use raw strings (r"...") for Windows file paths to avoid escape character issues

diabetes_model = pickle.load(open(r"diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"parkinsons_model.sav", 'rb'))


# ====================================================
# Sidebar Menu for Navigation
# ====================================================

with st.sidebar:
    selected = option_menu(
        menu_title='Multiple Disease Prediction System',
        options=['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )


# ====================================================
# 1. Diabetes Prediction Page
# ====================================================

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Machine Learning')

    # Create input fields in columns
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Level')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age')

    diab_diagnosis = ""

    # Prediction when button is clicked
    if st.button('Diabetes Test Result'):
        try:
            # Convert inputs to float and make prediction
            input_data = [[
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]]

            diab_prediction = diabetes_model.predict(input_data)

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is Diabetic'
            else:
                diab_diagnosis = 'The person is Not Diabetic'
        except:
            diab_diagnosis = ⚠️ Please enter all input fields as valid numbers.'

    st.success(diab_diagnosis)


# ====================================================
# 2. Heart Disease Prediction Page
# ====================================================

elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Machine Learning')

    # Input fields based on heart.csv dataset
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0–3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dl)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)')
    with col1:
        restecg = st.text_input('Resting ECG Results (0–2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment (0–2)')
    with col3:
        ca = st.text_input('Number of Major Vessels Colored (0–3)')
    with col1:
        thal = st.text_input('Thal (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)')

    heart_diagnosis = ""

    # Prediction when button is clicked
    if st.button('Heart Disease Test Result'):
        try:
            # Convert all inputs to float
            input_data = [[
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]]

            heart_prediction = heart_disease_model.predict(input_data)

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has Heart Disease'
            else:
                heart_diagnosis = 'The person does NOT have Heart Disease'
        except:
            heart_diagnosis = '⚠️ Please enter all input fields as valid numbers.'

    st.success(heart_diagnosis)


# ====================================================
# 3. Parkinson’s Disease Prediction Page
# ====================================================

elif selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using Machine Learning")

    # Input fields based on parkinsons.csv
    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col1:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        shimmer = st.text_input('MDVP:Shimmer')
    with col3:
        rap = st.text_input('MDVP:RAP')
    with col1:
        ddp = st.text_input('MDVP:PPQ')
    with col2:
        spread1 = st.text_input('spread1')
    with col3:
        spread2 = st.text_input('spread2')
    with col1:
        d2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ""

    # Prediction when button is clicked
    if st.button("Parkinson's Test Result"):
        try:
            input_data = [[
                float(fo), float(fhi), float(flo), float(jitter_percent),
                float(shimmer), float(rap), float(ddp),
                float(spread1), float(spread2), float(d2), float(PPE)
            ]]

            parkinsons_prediction = parkinsons_model.predict(input_data)

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's Disease"
            else:
                parkinsons_diagnosis = "The person does NOT have Parkinson's Disease"
        except:
            parkinsons_diagnosis = "⚠️ Please enter all input fields as valid numbers."

    st.success(parkinsons_diagnosis)
