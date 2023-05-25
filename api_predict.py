import requests

url = 'http://localhost:5000/api'

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
print(r.json)