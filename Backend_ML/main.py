from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle
#from joblib import load
import pandas as pd


model_name = "Credit card Fraud"
version = "v1.0.0"

class Details(BaseModel):  
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float
# class Details(BaseModel):
#     f_name: str
#     l_name: str
#     phone_number: int
 
with open('model.pickle','rb') as f:
    model=pickle.load(f)
#model=load("clasificacion_pipeline.joblib")


# Declaring our FastAPI instance
app = FastAPI()
 
# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Fraud credit card API'}
 
# Defining path operation for /name endpoint



def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction.item()


@app.post('/pred')
async def get_response(data:Details):
    X = pd.json_normalize(data.__dict__)
    prediction = predict(X, model)
    if prediction == 1:
        label = "Fraude"
    else:
        label = "No_fraude"
    return {
        'label': label,
        'prediction': int(prediction)
    }
    #df= pd.DataFrame([data.dict().values()],columns=data.dict().keys())
    #df = pd.DataFrame(data, index=[0])
    #prediction=model.predict(df)[0]
    ##X = pd.json_normalize(data.__dict__)
    ##prediction=model.predict(X)
    #test_1=data
    #V1=test_1['V1']
    ##return prediction[0].item() #{"Prediction":test_1[0]}
    #return {'message': df}
    
@app.get('/info')
async def model_info():
    """Return model information, version, how to call"""
    return {
        "name": model_name,
        "version": version
    }


#if __name__ == '__main__':
 #   uvicorn.run("main:app", host='127.0.0.1', port=4000, debug=True)
    