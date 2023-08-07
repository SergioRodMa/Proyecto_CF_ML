import streamlit as st
#from utils import PrepProcesor, columns 
import json

import requests
import time

import numpy as np
import pandas as pd
#import joblib

#api_key='AIzaSyAMk_kzSpHLypU3IyY0TjoIPVqek-eQhhg'

#params = {
#    "key": api_key
#}



columnas=["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14",
          "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28",
          "Amount"]

#model = joblib.load('xgbpipe.joblib')
st.title('¿Esta transaccion es fraudulenta? :credit_card: :money_with_wings:')

st.markdown('Variables Anonimas a llenar :currency_exchange:')


V1 = st.number_input("Variable Anonima 1",step=1.,format="%.4f",value =-1.3598071336738)
V2 = st.number_input("Variable Anonima 2",step=1.,format="%.4f",value =-0.0727811733098497)
V3 = st.number_input("Variable Anonima 3",step=1.,format="%.4f",value =2.53634673796914)
V4 = st.number_input("Variable Anonima 4",step=1.,format="%.4f",value =1.37815522427443)
V5 = st.number_input("Variable Anonima 5",step=1.,format="%.4f",value =-0.338320769942518)
V6 = st.number_input("Variable Anonima 6",step=1.,format="%.4f",value =0.462387777762292)
V7 = st.number_input("Variable Anonima 7",step=1.,format="%.4f",value =0.239598554061257)
V8 = st.number_input("Variable Anonima 8",step=1.,format="%.4f",value =0.0986979012610507)
V9= st.number_input("Variable Anonima 9",step=1.,format="%.4f",value =0.363786969611213)
V10 = st.number_input("Variable Anonima 10",step=1.,format="%.4f",value =0.0907941719789316)
V11 = st.number_input("Variable Anonima 11",step=1.,format="%.4f",value =-0.551599533260813)
V12 = st.number_input("Variable Anonima 12",step=1.,format="%.4f",value =-0.617800855762348)
V13 = st.number_input("Variable Anonima 13",step=1.,format="%.4f",value =-0.991389847235408)
V14 = st.number_input("Variable Anonima 14",step=1.,format="%.4f",value =-0.311169353699879)
V15 = st.number_input("Variable Anonima 15",step=1.,format="%.4f",value =1.46817697209427)
V16 = st.number_input("Variable Anonima 16",step=1.,format="%.4f",value =-0.470400525259478)
V17 = st.number_input("Variable Anonima 17",step=1.,format="%.4f",value =0.207971241929242)
V18 = st.number_input("Variable Anonima 18",step=1.,format="%.4f",value =0.0257905801985591)
V19 = st.number_input("Variable Anonima 19",step=1.,format="%.4f",value =0.403992960255733)
V20 = st.number_input("Variable Anonima 20",step=1.,format="%.4f",value =0.251412098239705)
V21 = st.number_input("Variable Anonima 21",step=1.,format="%.4f",value =-0.018306777944153)
V22 = st.number_input("Variable Anonima 22",step=1.,format="%.4f",value =0.277837575558899)
V23 = st.number_input("Variable Anonima 23",step=1.,format="%.4f",value =-0.110473910188767)
V24 = st.number_input("Variable Anonima 24",step=1.,format="%.4f",value =0.0669280749146731)
V25 = st.number_input("Variable Anonima 25",step=1.,format="%.4f",value =0.128539358273528)
V26 = st.number_input("Variable Anonima 26",step=1.,format="%.4f",value =-0.189114843888824)
V27 = st.number_input("Variable Anonima 27",step=1.,format="%.4f",value =0.133558376740387)
V28 = st.number_input("Variable Anonima 28",step=1.,format="%.4f",value =-0.0210530534538215)

st.markdown('Importe de la transaccion :moneybag:')
Amount = st.number_input("Cantidad",step=1.,format="%.2f",value =149.62)
# }

valores = [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14,
          V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28,
          Amount]

my_dictionary = dict(zip(columnas,valores))
payload = json.dumps(my_dictionary)

headers = {
  'Content-Type': 'application/json'
}

#url = "http://127.0.0.1:8000/pred" <- local
url = "https://fastapimlcf.ue.r.appspot.com/pred"

def predict(url,headers,payload):
    response = requests.request("POST", url, headers=headers, data=payload)
    data_dict = json.loads(response.text)
    if data_dict["prediction"] == 1:
        st.toast('Revisando tu transaccion')
        time.sleep(2)
        st.toast('Transaccion Fraudulenta :thumbdown: :anger:')
        st.error('Fraude! :thumbsdown:')
        time.sleep(20)
    else:
        #st.write('The current number is ', payload)
        st.toast('Revisando tu transaccion')
        time.sleep(2)
        st.balloons()
        st.toast('Transaccion segura :clap: :sparkles:')
        st.success('Transaccion segura :thumbsup:')
        time.sleep(20)

trigger = st.button('Predict', on_click=predict,args=(url,headers,payload))

