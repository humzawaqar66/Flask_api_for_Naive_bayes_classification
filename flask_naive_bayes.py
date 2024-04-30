import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)

with open('naive_bayes_classify.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/predict', methods=['POST'])

def predict():
    data = request.json
    
    if data['outlook'] == 'sunny':
        data['outlook'] = 2

    elif data['outlook'] == 'overcast':
        data['outlook'] = 0

    elif data['outlook'] == 'rainy':
        data['outlook'] = 1
    
    if data['temp']== 'hot':
        data['temp'] = 1
    
    elif data['temp']== 'mild':
        data['temp'] = 2
    
    elif data['temp']== 'cold':
        data['temp'] = 0
    
    if data['humidity']== 'high':
        data['humidity'] = 0
    
    elif data['humidity']== 'normal':
        data['humidity'] = 1
    
    if data['windy']== False:
        data['windy'] = 0
    elif data['windy']== True:
        data['windy'] = 1

    new = pd.DataFrame.from_dict([data])
    prediction = loaded_model.predict(new)

    play_mapping = {0: 'no_play', 1: 'yes_play'}

    label = play_mapping[prediction[0]]
    print(label)

    return jsonify({'prediction':label})

if __name__ == '__main__':
    app.run(debug=True)
