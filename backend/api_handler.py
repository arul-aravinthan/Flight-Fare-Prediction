from flask_restful import Resource
from flask import request
flight_data = {}

#API for getting and setting flight data
class ApiHandler(Resource):
    def get(self):
        return flight_data, 200
    
    def post(self):
        global flight_data
        flight_data = request.get_data().decode('utf-8')
        return {"status": "Success"}, 200