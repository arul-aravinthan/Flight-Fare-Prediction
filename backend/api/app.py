import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
import dill
from flask_restful import Api
from flask_cors import CORS
import json


app = Flask(__name__)
api = Api(app)
CORS(app) 
#Load pickled model and label encoders
model = dill.load(open('model.pkl', 'rb'))
column_order = dill.load(open('column_order.pkl', 'rb'))
ct = dill.load(open('ct.pkl', 'rb'))

@app.route("/", defaults={'path':''},  methods = ['GET', 'POST'])
@app.route("/<path:path>", methods = ['GET', 'POST'])
def api(path):
    if request.method == 'GET':
        return 'Welcome to the backend!'
    elif request.method == 'POST':
        data = request.get_data().decode('utf-8')
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

        input_features = ct.transform(input_features)

        prediction = model.predict(input_features)
        output = np.float64(prediction[0])
        return jsonify({'price': output})

if __name__ == '__main__':
    app.run(port=5000, debug=True)