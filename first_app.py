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
    
    PhoneService = st.text_input('Monthly Charges How Much?')
    
    MultipleLine = st.text_input('Total Charges how much?')
    
    InternetService = st.text_input('Multiple_Line_No phone service?if no answer 1 else 0')
    
    OnlineSecurity = st.text_input('Got online backup?0 or 1')
    
    
    OnlineBackup = st.text_input('Internet_Service_Fiber optic?0 or 1')
    
    DeviceProtection = st.text_input('Internet_Service_No? no is 1 yes 0')
    
    TechSupport = st.text_input('Online_Security_No internet service?no is 1 yes 0')
    
    StreamingTV = st.text_input('Online_Security_Yes? yes 1 no 0')
        
        
    StreamingMovies = st.text_input('Online_Backup_No internet service?no is 1')
    
    Contract = st.selectbox('Do you have any contract?', ('Month-to-month', 'One year', 'Two year'))
    
    PaperlessBilling = st.text_input('DeviceProtection_No internet service?')
    
    PaymentMethod = st.text_input('DeviceProtection_Yes? yes 1 else 0')
    
    MonthlyCharges = st.slider('What is your monthly charges?',0,119,30)
    
        
    TotalCharges = st.slider('What is your total charges?',0,8685,500)
    
    
    Gender = st.text_input('StreamingTV_No internet service?')
    
    SeniorCitizen = st.text_input('StreamingTV_Yes?')
    
    Partner = st.text_input('StreamingMovies_Yes?')
    
    Dependents = st.text_input('StreamingMovies_No internet service?')
            
    tenuregroup = st.text_input('Contract_One year? if yes 1 no 0')
    
    
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




