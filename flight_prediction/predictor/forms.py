from django import forms

class PredictionForm(forms.Form):
    Total_Stops = forms.IntegerField(label='Total Stops')
    Journey_day = forms.IntegerField(label='Journey Day')
    Journey_month = forms.IntegerField(label='Journey Month')
    Dep_hour = forms.IntegerField(label='Departure Hour')
    Dep_min = forms.IntegerField(label='Departure Minute')
    Arrival_hour = forms.IntegerField(label='Arrival Hour')
    Arrival_min = forms.IntegerField(label='Arrival Minute')
    Duration_hours = forms.IntegerField(label='Duration Hours')
    Duration_mins = forms.IntegerField(label='Duration Minutes')
    Airline = forms.ChoiceField(choices=[
        ('Air India', 'Air India'),
        ('GoAir', 'GoAir'),
        ('IndiGo', 'IndiGo'),
        ('Jet Airways', 'Jet Airways'),
        ('Jet Airways Business', 'Jet Airways Business'),
        ('Multiple carriers', 'Multiple carriers'),
        ('Multiple carriers Premium economy', 'Multiple carriers Premium economy'),
        ('SpiceJet', 'SpiceJet'),
        ('Trujet', 'Trujet'),
        ('Vistara', 'Vistara'),
        ('Vistara Premium economy', 'Vistara Premium economy')
    ])
    Source = forms.ChoiceField(choices=[
        ('Chennai', 'Chennai'),
        ('Delhi', 'Delhi'),
        ('Kolkata', 'Kolkata'),
        ('Mumbai', 'Mumbai')
    ])
    Destination = forms.ChoiceField(choices=[
        ('Cochin', 'Cochin'),
        ('Delhi', 'Delhi'),
        ('Hyderabad', 'Hyderabad'),
        ('Kolkata', 'Kolkata'),
        ('New Delhi', 'New Delhi')
    ])
