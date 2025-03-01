from fastapi import FastAPI
import joblib
import numpy as np
import configparser
import os
import boto3

# Reading Access and Secret Key
config = configparser.ConfigParser()
config.read("app/.awscredentials")
AWS_ACCESS_KEY = config['default']['aws_access_key_id']
AWS_SECRET_KEY = config['default']['aws_secret_access_key']
S3_BUCKET_NAME = config['default']['bucket_name']
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
    """
    Predict the class name based on the provided features.
    Args:
        data (dict): A dictionary containing the input data. 
                        The dictionary should have a key 'features' 
                        which maps to a list or array of feature values.
    Returns:
        dict: A dictionary containing the prediction result with the key 'prediction' 
                mapping to the predicted class name.
    Example:
        data = {
            "features": [0.5, 1.2, 3.4, 2.1]
        }
        result = predict(data)
        # result will be something like {'prediction': 'class_name'}
    """
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'prediction': class_name}