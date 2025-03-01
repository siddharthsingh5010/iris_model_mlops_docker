Model Experimentation, Deployment and Serving with MLFlow and Docker

This project demonstrates the training, experimentation, and deployment of a Random Forest model on the Iris dataset. The workflow includes model tracking with MLFlow, best model selection based on accuracy, storage in S3, and serving the model using Docker.

🚀 Features
	1.	Model Training & Experimentation:
	•	Uses MLFlow to track multiple experiments.
	•	Trains a Random Forest model on the Iris dataset.
	•	Logs model metrics, parameters, and artifacts.
	2.	Best Model Selection & Storage:
	•	Selects the best model based on accuracy.
	•	Saves the best model to an S3 bucket.
	•	Registers the model in MLFlow and moves it to the Production stage.
	3.	Model Deployment with Docker:
	•	Downloads the production-ready model from S3.
	•	Deploys the model using FastAPI.
	•	Runs the server on port 8080.

🛠 Setup Instructions

1️⃣ Install Dependencies

Ensure you have Python installed and then install the required dependencies:

pip install -r requirements.txt

2️⃣ Configure AWS Credentials

To enable uploading/downloading the model from S3, add your AWS credentials.

🔹 Root Directory AWS Config

Create a .aws/credentials file in the root directory:

[default]
aws_access_key_id = YOUR_AWS_ACCESS_KEY
aws_secret_access_key = YOUR_AWS_SECRET_KEY

🔹 Model Serving AWS Config

Create a separate AWS config file inside the model_serving/ folder:

touch model_serving/.awscredentials

Add the following:

[default]
aws_access_key_id = YOUR_AWS_ACCESS_KEY
aws_secret_access_key = YOUR_AWS_SECRET_KEY
bucket_name = YOUR_S3_BUCKET_NAME

🚀 Running the Project

1 Train & Experiment with MLFlow

Run the training script to log experiments in MLFlow:

experiment/1_training.ipynb

This will:
	•	Log all experiments in MLFlow.

2 Log the Best Model

experiment/2_best_model_selection.ipynb

This will:
	•	Select the best model based on accuracy.
	•	Register the best model and transition it to Production.
	•	Upload the model to S3.

3 Serve the Model via Docker

🔹 Build the Docker Image (model_serving)

docker build -t iris_model_serving .

🔹 Run the Container

docker run -p 8080:8080 iris_model_serving

This will:
	•	Download the best model from S3.
	•	Start a FastAPI server on port 8080 to serve predictions.

📡 API Endpoint

Once the server is running, you can send POST requests to make predictions.

🔹 Request Example

curl -X POST "http://localhost:8080/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [1.2,3.5,4.6,5.1]}'

🔹 Response Example

{
  "prediction": "setosa"
}

📌 Notes
	•	Ensure the AWS credentials are configured before running the scripts.
	•	The best model is automatically selected based on accuracy and stored in S3.
	•	The Docker container will pull the production-ready model from S3 at runtime.