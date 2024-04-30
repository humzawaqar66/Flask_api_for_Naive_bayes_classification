Tennis Play Prediction API
This repository contains code for a Flask API that predicts whether to play tennis based on weather conditions using a trained Gaussian Naive Bayes classifier.

Overview
The API utilizes a machine learning model trained on a dataset containing weather conditions and corresponding decisions to play tennis. The model predicts whether to play tennis based on four features: outlook, temperature, humidity, and windiness.

Installation
Clone this repository to your local machine using git clone https://github.com/your_username/tennis-play-prediction.git.
Navigate to the project directory: cd tennis-play-prediction.
Create a virtual environment: python -m venv venv.
Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS and Linux: source venv/bin/activate
Install the required dependencies: pip install -r requirements.txt.

Usage
Ensure that the virtual environment is activated.
Run the Flask application:
Copy code
python app.py
Once the server is running, send a POST request to http://localhost:5000/predict with JSON data containing weather features: outlook, temperature, humidity, and windiness.
Example JSON data:
json
Copy code
{
    "outlook": "sunny",
    "temp": "hot",
    "humidity": "high",
    "windy": false
}
You will receive a JSON response with the predicted decision: "yes_play" or "no_play".
Model Training
The model used by the API is trained using a Gaussian Naive Bayes classifier. The training code is available in the Jupyter Notebook model_training.ipynb.

File Structure
app.py: Flask application script containing API endpoints.
model_training.ipynb: Jupyter Notebook containing code for training the machine learning model.
naive_bayes_model.pkl: Serialized trained model saved using pickle.
tennis.csv: Dataset used for model training.
requirements.txt: List of Python dependencies.
License
This project is licensed under the MIT License. See the LICENSE file for details.
