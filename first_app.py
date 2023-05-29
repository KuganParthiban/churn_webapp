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
    
    MonthlyCharges = st.sidebar.slider('What is your monthly charges?',0,119,30)
    
    TotalCharges = st.sidebar.slider('What is your total charges?',0,8685,500)
    
    PhoneService = st.selectbox('Do you have phone service?', ('Yes', 'No'))
    
    MultipleLine = st.selectbox('Do you have multiple lines?', ('Yes', 'No', 'No phone service'))
    
    InternetService = st.selectbox('Got internet service?', ('DSL', 'Fiber Optic', 'No'))
    
    OnlineSecurity = st.selectbox('Got online security?', ('Yes', 'No', 'No internet service'))
    
    OnlineBackup = st.selectbox('Got online backup?', ('Yes', 'No', 'No internet service'))
    
    DeviceProtection = st.selectbox('Got device protection?', ('Yes', 'No', 'No internet service'))
    
    TechSupport = st.selectbox('Got tech support?', ('Yes', 'No', 'No internet service'))
    
    StreamingTV = st.selectbox('Got streaming tv?', ('Yes', 'No', 'No internet service'))
        
    StreamingMovies = st.selectbox('Got streaming movies?', ('Yes', 'No', 'No internet service'))
    
    Contract = st.selectbox('Do you have any contract?', ('Month-to-month', 'One year', 'Two year'))
    
    PaperlessBilling = st.selectbox('got paperless billing?', ('Yes', 'No'))
    
    PaymentMethod = st.selectbox('Select your payment method', ('Electronic check','Mailed check','Bank transfer (automatic)', 'Credit card (automatic)'))
  
    Gender = st.selectbox('Gender', ('Female', 'Male'))
    
    SeniorCitizen = st.selectbox('Are you a senior citizen?', ('Yes', 'No'))
    
    Partner = st.selectbox('Are you a senior citizen?', ('Yes', 'No'))
    
    Dependents = st.selectbox('got any dependents?', ('Yes', 'No'))
            
    tenuregroup = st.selectbox('How long is your tenure?', ('1 - 12', '25 - 36', '37 - 48', '13 - 24', '61 - 72', '49 - 60'))
    
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




