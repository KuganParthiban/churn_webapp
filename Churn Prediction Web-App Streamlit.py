#!/usr/bin/env python
# coding: utf-8

# In[17]:


#import library
import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model = pickle.load(open('model_churn.sav','rb'))


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
    
    Phone_Service = st.text_input('Do you take any mobile services?')
    Multiple_Line = st.text_input('Do you own multiple lines?')
    Internet_Service = st.text_input('Got internet service?')
    Online_Security = st.text_input('Got online security?')
    Online_Backup = st.text_input('Got online backup?')
    Device_Protection = st.text_input('Got device protection?')
    Tech_Support = st.text_input('Got tech support?')
    Streaming_TV = st.text_input('Got StreamingTV?')
    Streaming_Movies = st.text_input('Got StreamingMovies?')
    Contract = st.text_input('Contract?')
    Paperless_Billing = st.text_input('PaperlessBilling?')
    Payment_Method = st.text_input('PaymentMethod?')
    Monthly_Charges = st.text_input('MonthlyCharges?')
    Total_Charges = st.text_input('TotalCharges?')
    Gender = st.text_input('Gender?')
    Senior_Citizen = st.text_input('Are you a senior citizen?')
    Partner = st.text_input('Got Partner?')
    Dependents = st.text_input('Got Dependents?')
    tenure_group = st.text_input('tenure_group?')

    
    
    # code for prediction
    
    diagnosis = ''
    
    
    # creating a button for prediction
    
    if st.button('Churn Result'):
        diagnosis = churn_prediction([Phone_Service,Multiple_Line,Internet_Service,
                                     Online_Security, Online_Backup, Device_Protection,
                                     Tech_Support,Streaming_TV,Streaming_Movies,
                                     Contract,Paperless_Billing,Payment_Method,
                                     Monthly_Charges,Total_Charges,Gender,
                                     Senior_Citizen,Partner,Dependents,tenure_group])
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()


# In[ ]:




