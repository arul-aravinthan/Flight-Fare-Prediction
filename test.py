import pickle
import pandas as pd


model = pickle.load(open('model.pkl', 'rb'))
label_encoders = pickle.load(open('label_encoders.pkl', 'rb'))
std = pickle.load(open('std.pkl', 'rb'))
data = {'airline': "AirAsia", 'source_city': 'Bangalore', 'departure_time': 'Early_Morning', 'stops': 'zero', 'arrival_time': 'Evening',
                                  'destination_city': 'Kolkata', 'class': 'Economy', 'duration': 1, 'days_left' : 15}

for i, column in enumerate(data):
    if type(data[column]) == str:
        data[column] = label_encoders[column].transform([data[column]])[0]
input_features = pd.DataFrame(data, index=[0])
input_features = std.transform(input_features)
print(model.predict(input_features))