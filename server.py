import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import pickle
from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
import requests
from api_handler import ApiHandler

app = Flask(__name__)
api = Api(app)
model = pickle.load(open('model.pkl', 'rb'))
label_encoders = pickle.load(open('label_encoders.pkl', 'rb'))

@app.route("/", defaults={'path':''})
def main(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(ApiHandler, '/flask/hello')


@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    r = requests.post('http://localhost:5000/api' ,json={'airline': "SpiceJet",
                             'source_city': "Delhi",
                             'departure_time': "Evening", 
                             'stops': 2,
                             'arrival_time': "Night", 
                             'destination_city': "Mumbai", 
                             'class': "Economy",
                             'duration': 2.17,
                             'days_left': 1,  
                             })
    
    data = r.json
    # Make prediction using model loaded from disk as per the data.
    for i, column in enumerate(data):
        if type(data[column]) == str:
            data[column] = label_encoders[i].transform([data[column]])[0]
    print(data)
    prediction = model.predict(pd.DataFrame([data]))
    output = prediction[0]
    print(output)
    return jsonify(output)


if __name__ == '__main__':
    app.run(port=5000, debug=True)