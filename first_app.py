#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import library
import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model = pickle.load(open('churn_predict.pkl','rb'))


# creating a function for prediction

def churn_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not churn'
    else:
      return 'The person is churn'
    


def main():
    
    
    #giving a title 
    st.title('Churn Prediction Web App')
    
    
    #getting the input data from the user
    
    PhoneService = st.selectbox('Do you have phone service?', ('Yes', 'No'), key="phone_service_key")
    MultipleLine = st.selectbox('Do you have multiple lines?', ('Yes', 'No', 'No phone service'), key="multiple_line_key")
    InternetService = st.selectbox('Got internet service?', ('DSL', 'Fiber Optic', 'No'), key="internet_service_key")
    OnlineSecurity = st.selectbox('Got online security?', ('Yes', 'No', 'No internet service'), key="online_security_key")
    OnlineBackup = st.selectbox('Got online backup?', ('Yes', 'No', 'No internet service'), key="online_backup_key")
    DeviceProtection = st.selectbox('Got device protection?', ('Yes', 'No', 'No internet service'), key="device_protection_key")
    TechSupport = st.selectbox('Got tech support?', ('Yes', 'No', 'No internet service'), key="tech_support_key")
    StreamingTV = st.selectbox('Got streaming TV?', ('Yes', 'No', 'No internet service'), key="streaming_tv_key")
    StreamingMovies = st.selectbox('Got streaming movies?', ('Yes', 'No', 'No internet service'), key="streaming_movies_key")
    Contract = st.selectbox('Do you have any contract?', ('Month-to-month', 'One year', 'Two year'), key="contract_key")
    PaperlessBilling = st.selectbox('Got paperless billing?', ('Yes', 'No'), key="paperless_billing_key")
    PaymentMethod = st.selectbox('Select your payment method', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'), key="payment_method_key")
    Gender = st.selectbox('Gender', ('Female', 'Male'), key="gender_key")
    SeniorCitizen = st.selectbox('Are you a senior citizen?', ('Yes', 'No'), key="senior_citizen_key")
    Partner = st.selectbox('Do you have a partner?', ('Yes', 'No'), key="partner_key")
    Dependents = st.selectbox('Do you have any dependents?', ('Yes', 'No'), key="dependents_key")
    tenuregroup = st.selectbox('How long is your tenure?', ('1 - 12', '25 - 36', '37 - 48', '13 - 24', '61 - 72', '49 - 60'), key="tenure_group_key")
    MonthlyCharges = st.sidebar.slider('What is your monthly charges?', 18,119,70)
    TotalCharges = st.sidebar.slider('What is your total charges?', 18,8685,1397)
    

    
    # code for prediction
    
    diagnosis = ''
    
    
    # creating a button for prediction
    
    if st.button('Churn Result'):
        diagnosis = churn_prediction(['Phone Service',
 'MultipleLine',
 'InternetService',
 'OnlineSecurity',
 'OnlineBackup',
 'DeviceProtection',
 'TechSupport',
 'StreamingTV',
 'StreamingMovies',
 'Contract',
 'PaperlessBilling',
 'PaymentMethod',
 'MonthlyCharges',
 'TotalCharges',
 'Gender',
 'SeniorCitizen',
 'Partner',
 'Dependents',
 'tenuregroup'])
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()


# In[ ]:




