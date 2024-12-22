import React, { useState } from 'react';
import axios from 'axios';

function FlightPricePrediction() {
    const [formData, setFormData] = useState({
        Total_Stops: 1,
        Journey_day: 24,
        Journey_month: 3,
        Dep_hour: 14,
        Dep_min: 30,
        Arrival_hour: 16,
        Arrival_min: 45,
        Duration_hours: 2,
        Duration_mins: 15,
        Airline: "Jet Airways",
        Source: "Delhi",
        Destination: "Cochin"
    });

    const [prediction, setPrediction] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://127.0.0.1:8000/predict/', formData)
            .then(response => {
                setPrediction(response.data.prediction_text);
            })
            .catch(error => {
                console.error('There was an error!', error);
            });
    };

    return (
        <div className="container"  style={{ 
            backgroundImage: `url(${process.env.PUBLIC_URL + '/background.webp'})`, 
            backgroundSize: 'cover', 
            backgroundPosition: 'center',
            height: '100vh' // Adjust as needed
        }}>
            <h4 style={{textAlign:'center',fontFamily:'sans-serif',fontWeight:'900'}}>FLIGHT FARE PREDICTION</h4>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="Dep_Time">Departure Time</label>
                    <input
                        type="datetime-local"
                        className="form-control"
                        id="Dep_Time"
                        name="Dep_Time"
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="Arrival_Time">Arrival Time</label>
                    <input
                        type="datetime-local"
                        className="form-control"
                        id="Arrival_Time"
                        name="Arrival_Time"
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="Source">Source</label>
                    <select className="form-control" id="Source" name="Source" onChange={handleChange} required>
                        <option value="Delhi">Delhi</option>
                        <option value="Kolkata">Kolkata</option>
                        <option value="Mumbai">Mumbai</option>
                        <option value="Chennai">Chennai</option>
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="Destination">Destination</label>
                    <select className="form-control" id="Destination" name="Destination" onChange={handleChange} required>
                        <option value="Cochin">Cochin</option>
                        <option value="Delhi">Delhi</option>
                        <option value="New Delhi">New Delhi</option>
                        <option value="Hyderabad">Hyderabad</option>
                        <option value="Kolkata">Kolkata</option>
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="Total_Stops">Stopage</label>
                    <select className="form-control" id="Total_Stops" name="Total_Stops" onChange={handleChange} required>
                        <option value="0">Non-Stop</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="Airline">Which Airline you want to travel?</label>
                    <select className="form-control" id="Airline" name="Airline" onChange={handleChange} required>
                        <option value="Jet Airways">Jet Airways</option>
                        <option value="IndiGo">IndiGo</option>
                        <option value="Air India">Air India</option>
                        <option value="Multiple carriers">Multiple carriers</option>
                        <option value="SpiceJet">SpiceJet</option>
                        <option value="Vistara">Vistara</option>
                        <option value="GoAir">GoAir</option>
                        <option value="Multiple carriers Premium economy">Multiple carriers Premium economy</option>
                        <option value="Jet Airways Business">Jet Airways Business</option>
                        <option value="Vistara Premium economy">Vistara Premium economy</option>
                        <option value="Trujet">Trujet</option>
                    </select>
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
            {prediction && <h3>{prediction}</h3>}
        </div>
    );
}

export default FlightPricePrediction;
