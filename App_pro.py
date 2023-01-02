
import pickle
import streamlit as st


# loading the saved models

startUp_model = pickle.load(open('Model/random_model.sav', 'rb'))

    
    
# page title
st.title('StartUp_model Prediction using ML')
    
    
# getting the input data from the user
col1, col2, col3 = st.columns(3)
    
with col1:
    name = st.text_input('Name of StartUp')
        
with col2:
    market = st.text_input('market name')
    
with col3:
    funding_total_usd = st.text_input('funding_total_usd')
    
with col1:
    region = st.text_input('region')
    
with col2:
    funding_rounds = st.text_input('funding_rounds')
    
with col3:
    founded_year = st.text_input('founded_year')
    
with col1:
    seed = st.text_input('seed')
    
with col2:
    venture = st.text_input('venture value')

with col3:
    equity_crowdfunding = st.text_input('equity_crowdfunding')

with col1:
    angel = st.text_input('angel value')
    
with col2:
    grant = st.text_input('grant value')

with col3:
    private_equity = st.text_input('private_equity value')

with col1:
    product_crowdfunding = st.text_input('product_crowdfunding')
    
with col2:
    round_A = st.text_input('round_A')

with col3:
    round_B = st.text_input('round_B')

with col1:
    country = st.text_input('country')
    
    
# code for Prediction
diab_diagnosis = ''
    
# creating a button for Prediction
    
if st.button('startUp model Test Result'):
    StartUp_prediction = startUp_model.predict([[name, market, funding_total_usd, region, funding_rounds, founded_year, seed, venture,equity_crowdfunding,angel,grant,private_equity,product_crowdfunding,round_A,round_B,country]])
        
    if (StartUp_prediction[0] == 0):
        diab_diagnosis = 'Your StartUp is operating'
    elif(StartUp_prediction[0] == 1):
        diab_diagnosis = 'Your StartUp is acquired'
    else:
        diab_diagnosis = 'Your StartUp is closed'
        
st.success(diab_diagnosis)
