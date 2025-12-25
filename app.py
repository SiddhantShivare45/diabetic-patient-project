import streamlit as st
import pandas as pd 
import pickle as pkl

scaler=pkl.load(open('scaler.pkl','rb'))
model=pkl.load(open('model.pkl','rb'))

st.title("Daibetic Patient Prediction Project")
gender=st.selectbox("Select Gender",['Female','Male','other'])
age=st.number_input("Enter Age ",min_value=0,max_value=100,value=50)
hypertension=st.selectbox("Select Hypertension",["Yes","No"])
heart_diseases=st.selectbox("Select Heart Disease",["Yes","No"])
smoking_histroy=st.selectbox("Select Somokings",['Never', 'No Info', 'Former','Not Current','Ever','Current' ])
bmi=st.number_input("Enter BMI ",min_value=20,max_value=50,value=28)
HbA1c_level=st.number_input("Enter HBA1C Level ",min_value=5.0,max_value=10.0,value=6.6,step=0.1)
blood_glucose_level=st.number_input("Enter Blood Glucose Level ",min_value=25 ,max_value=500,value=200)

if gender=='Female':
    gender=0
elif gender=='Male':
    gender=1
else:
    gender=2

if smoking_histroy=='Never':
    smoking_histroy=0
elif smoking_histroy=='No Info':
     smoking_histroy=1
elif smoking_histroy=='Former' or smoking_histroy== 'Not Current':
    smoking_histroy=2
elif smoking_histroy=='Ever':
    smoking_histroy=3
else:
    smoking_histroy=4


if hypertension=='Yes':
    hypertension=1
else:
    hypertension=0

if heart_diseases=='Yes':
    heart_diseases=1
else:
   heart_diseases=0

if st.button("Predict"):
    myinput=[[gender,age,hypertension,heart_diseases,smoking_histroy,bmi,HbA1c_level,blood_glucose_level]]
    columns=['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history','bmi', 'HbA1c_level', 'blood_glucose_level']
    data= pd.DataFrame(data=myinput,columns= columns)
    data_scaled=scaler.transform(data)
    result=model.predict(data_scaled)
    if result[0]==1:
        st.error("Person in daibetic")
    else:
        st.success("Person is Not daibetic")

 
