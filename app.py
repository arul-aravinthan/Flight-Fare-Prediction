import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import pickle
from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import requests
from api_handler import ApiHandler
import json

app = Flask(__name__)
api = Api(app)
CORS(app) 
#Load pickled model and label encoders
model = pickle.load(open('model.pkl', 'rb'))
label_encoders = pickle.load(open('label_encoders.pkl', 'rb'))
column_order = pickle.load(open('column_order.pkl', 'rb'))
std = pickle.load(open('std.pkl', 'rb'))
@app.route("/", defaults={'path':''})
def main(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(ApiHandler, '/api')


@app.route('/predict')
def predict():
    data = requests.get('http://localhost:5000/api').json()
    data = json.loads(data)

    #Convert stops to categorical variable
    if data['stops'] == 0:
        data['stops'] = 'zero'
    elif data['stops'] == 1:
        data['stops'] = 'one'
    else:
        data['stops'] = 'two_or_more'
    # Make prediction using model loaded from disk as per the data.

    input_features = pd.DataFrame([], columns=column_order)
    input_features = pd.concat([input_features, pd.DataFrame(data, index=[0])], axis=0)

    input_features = std.transform(input_features['duration', 'days_left'])
    # Encode the categorical variables
    for column in input_features.columns:
        if column in label_encoders.keys():
            input_features[column] = label_encoders[column].transform([input_features[column]])[0]
    input_features['days_left'] = pd.to_numeric(input_features['days_left'])
    input_features['duration'] = pd.to_numeric(input_features['duration'])
    prediction = model.predict(input_features)
    output = np.float64(prediction[0])
    return jsonify({'price': output})


if __name__ == '__main__':
    app.run(port=5000, debug=True)