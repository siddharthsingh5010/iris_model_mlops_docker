from fastapi import FastAPI
import joblib
import numpy as np

import boto3
# ABC 
# AWS S3 Configuration
AWS_ACCESS_KEY = "AKIASVQKHTXCBUOO4VP2"
AWS_SECRET_KEY = "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"
S3_BUCKET_NAME = "siddharthsingh5010mybucket"
S3_MODEL_PATH = "iris_model/model/best_model.pkl" 

LOCAL_MODEL_PATH = "app/models/best_model.pkl" 

s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
s3_client.download_file(S3_BUCKET_NAME, S3_MODEL_PATH, LOCAL_MODEL_PATH)

model = joblib.load('app/models/best_model.pkl')

class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()

@app.get("/")
def read_root():
    return {'message': 'Hello, World!'}

@app.post("/predict")
def predict(data:dict):
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'prediction': class_name}