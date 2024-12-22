# predictor/views.py

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open("E:/ue/dss all/dss/flight_rf_latest.pkl", "rb"))


@api_view(["POST"])
def predict_price(request):
    if request.method == "POST":
        data = request.data

        # Date_of_Journey
        date_dep = data.get("Dep_Time")
        Journey_day = int(pd.to_datetime(date_dep).day)
        Journey_month = int(pd.to_datetime(date_dep).month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep).hour)
        Dep_min = int(pd.to_datetime(date_dep).minute)

        # Arrival
        date_arr = data.get("Arrival_Time")
        Arrival_hour = int(pd.to_datetime(date_arr).hour)
        Arrival_min = int(pd.to_datetime(date_arr).minute)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)

        # Total Stops
        Total_stops = int(data.get("Total_Stops"))

        # Airline
        airline = data.get("Airline")
        airlines_dict = {
            'Jet Airways': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'IndiGo': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Air India': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            'Multiple carriers': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            'SpiceJet': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            'Vistara': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            'GoAir': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            'Multiple carriers Premium economy': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            'Jet Airways Business': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            'Vistara Premium economy': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            'Trujet': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        }

        airline_features = airlines_dict.get(airline, [0]*11)

        # Source
        source = data.get("Source")
        source_dict = {
            'Delhi': [1, 0, 0, 0],
            'Kolkata': [0, 1, 0, 0],
            'Mumbai': [0, 0, 1, 0],
            'Chennai': [0, 0, 0, 1]
        }

        source_features = source_dict.get(source, [0]*4)

        # Destination
        destination = data.get("Destination")
        destination_dict = {
            'Cochin': [1, 0, 0, 0, 0],
            'Delhi': [0, 1, 0, 0, 0],
            'New Delhi': [0, 0, 1, 0, 0],
            'Hyderabad': [0, 0, 0, 1, 0],
            'Kolkata': [0, 0, 0, 0, 1]
        }

        destination_features = destination_dict.get(destination, [0]*5)

        features = [Total_stops, Journey_day, Journey_month, Dep_hour, Dep_min,
                    Arrival_hour, Arrival_min, dur_hour, dur_min] + airline_features + source_features + destination_features

        # Ensure the length of features is 33 (the same as during training)
        print(features)
        while len(features) < 33:
            features.append(0)

        prediction = model.predict([features])
        output = round(prediction[0], 2)

        return JsonResponse({'prediction_text': f"Your Flight price is Rs. {output}"})
