import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks', layout='wide', page_icon="🧑‍⚕️")

diabetes_model = pickle.load(open(r"C:\Users\sowmy\Desktop\disease prediction\training models\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\sowmy\Desktop\disease prediction\training models\heart_k-nearest_neighbors_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\sowmy\Desktop\disease prediction\training models\parkinsons_k-nearest_neighbors_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        # Check if any of the fields are empty
        if '' in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]:
            st.error('Please fill in all the fields.')
        else:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            try:
                user_input = [float(x) for x in user_input]
                diab_prediction = diabetes_model.predict([user_input])
                if diab_prediction[0] == 1:
                    diab_diagnosis = "The person is diabetic."
                else:
                    diab_diagnosis = "The person is not diabetic."
                st.success(diab_diagnosis)
            except ValueError:
                st.error('Invalid input. Please enter numeric values.')
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (Male/Female)')
    with col3:
        cp = st.text_input('Chest Pain Type')  
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment')
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        # Check if any of the fields are empty
        if '' in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]:
            st.error('Please fill in all the fields.')
        else:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            try:
                user_input = [float(x) if isinstance(x, str) else x for x in user_input]  # Convert numeric input
                heart_prediction = heart_disease_model.predict([user_input])
                if heart_prediction[0] == 1:
                    heart_diagnosis = "The person has heart disease."
                else:
                    heart_diagnosis = "The person does not have heart disease."
                st.success(heart_diagnosis)
            except ValueError:
                st.error('Invalid input. Please enter numeric values.')

if selected == 'Parkinsons Prediction':
    st.title('Parkinson’s Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)')
    with col1:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')
    with col1:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button('Parkinson’s Test Result'):
        # Check if any of the fields are empty
        if '' in [MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ,
                  Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]:
            st.error('Please fill in all the fields.')
        else:
            user_input = [MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ,
                          Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            try:
                user_input = [float(x) for x in user_input]
                parkinsons_prediction = parkinsons_model.predict([user_input])
                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson’s disease."
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson’s disease."
                st.success(parkinsons_diagnosis)
            except ValueError:
                st.error('Invalid input. Please enter numeric values.')
