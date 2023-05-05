#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import library
import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model = pickle.load(open('first_deployment.sav','rb'))


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
    
    Monthly_Charges = st.text_input('Monthly Charges How Much?')
    
    Total_Charges = st.text_input('Total Charges how much?')
    
    Phone_Service_Yes = st.text_input('Phone_Service_Yes? If yes answer 1 else 0')
    
    Multiple_Line_No_phone_service = st.text_input('Multiple_Line_No phone service?if no answer 1 else 0')
    
    Multiple_Line_Yes = st.text_input('Got online backup?0 or 1')
    
    
    Internet_Service_Fiber_optic = st.text_input('Internet_Service_Fiber optic?0 or 1')
    
    Internet_Service_No = st.text_input('Internet_Service_No? no is 1 yes 0')
    
    Online_Security_No_internet_service = st.text_input('Online_Security_No internet service?no is 1 yes 0')
    
    Online_Security_Yes = st.text_input('Online_Security_Yes? yes 1 no 0')
        
        
    Online_Backup_No_internet_service = st.text_input('Online_Backup_No internet service?no is 1')
    
    Online_Backup_Yes = st.text_input('Online_Backup_Yes?yes is 1')
    
    DeviceProtection_No_internet_service = st.text_input('DeviceProtection_No internet service?no is 1')
    
    DeviceProtection_Yes = st.text_input('DeviceProtection_Yes? yes 1 else 0')
    
    TechSupport_No_internet_service = st.text_input('TechSupport_No internet service?')
    
        
    TechSupport_Yes = st.text_input('TechSupport_Yes?')
    
    StreamingTV_No_internet_service = st.text_input('StreamingTV_No internet service?')
    
    StreamingTV_Yes = st.text_input('StreamingTV_Yes?')
    
    StreamingMovies_Yes = st.text_input('StreamingMovies_Yes?')
    
    StreamingMovies_No_internet_service = st.text_input('StreamingMovies_No internet service?')
            
    Contract_One_year = st.text_input('Contract_One year? if yes 1 no 0')
    
    Contract_Two_year = st.text_input('Contract_Two year?')
    
    PaperlessBilling_Yes = st.text_input('PaperlessBilling_Yes?')
    
    PaymentMethod_Creditcard_automatic = st.text_input('PaymentMethod_Creditcardautomati?')
    
    PaymentMethod_Electronic_check = st.text_input('PaymentMethod_Electroniccheck?')
      
    PaymentMethod_Mailed_check = st.text_input('tPaymentMethod_Mailedcheck?')
    
    Gender_Male = st.text_input('Gender_Male?if male 1 else 0')
    
    Senior_Citizen_1 = st.text_input('Senior_Citizen_1?')
    
    Partner_Yes = st.text_input('Partner_Yes?')
    
    Dependents_Yes = st.text_input('Dependents_Yes?')
    
    tenure_group_13_24 = st.text_input('tenure_group_13 - 24?')
    
    tenure_group_25_36 = st.text_input('tenure_group_25 - 36?')
    
    tenure_group_37_48 = st.text_input('tenure_group_37 - 48?')
    
    tenure_group_49_60 = st.text_input('tenure_group_49 - 60?')
    
    tenure_group_61_72  = st.text_input('tenure_group_61 - 72 ?')
    
    

    
    
    # code for prediction
    
    diagnosis = ''
    
    
    # creating a button for prediction
    
    if st.button('Churn Result'):
        diagnosis = churn_prediction([Monthly_Charges, Total_Charges, Phone_Service_Yes,Multiple_Line_No_phone_service,
                                      Multiple_Line_Yes,Internet_Service_Fiber_optic,Internet_Service_No,
                                      Online_Security_No_internet_service, Online_Security_Yes,
                                      Online_Backup_No_internet_service, Online_Backup_Yes,
                                      DeviceProtection_No_internet_service, DeviceProtection_Yes,
                                      TechSupport_No_internet_service, TechSupport_Yes,
                                      StreamingTV_No_internet_service, StreamingTV_Yes,
                                      StreamingMovies_No_internet_service, StreamingMovies_Yes,
                                      Contract_One_year, Contract_Two_year, PaperlessBilling_Yes,
                                      PaymentMethod_Creditcard_automatic,
                                      PaymentMethod_Electronic_check, PaymentMethod_Mailed_check,
                                      Gender_Male, Senior_Citizen_1, Partner_Yes, Dependents_Yes,
                                      tenure_group_13_24, tenure_group_25_36, tenure_group_37_48,
                                      tenure_group_49_60, tenure_group_61_72])
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()


# In[ ]:




