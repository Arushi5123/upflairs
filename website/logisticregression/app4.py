from flask import Flask, render_template, url_for, request
import pandas as pd
import joblib

model = joblib.load('logisticregression.lb')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Flight_cust_satisfaction.html')

@app.route('/flight', methods=['GET', 'POST'])
def flight():
    if request.method == 'POST':
        age = int(request.form['age'])
        flight_distance = int(request.form['flight_distance'])
        inflight_entertainment = int(request.form['inflight_entertainment'])
        baggage_handling = int(request.form['baggage_handling'])
        cleanliness = int(request.form['cleanliness'])
        departure_delay = int(request.form['departure_delay'])
        arrival_delay = int(request.form['arrival_delay'])
        gender = int(request.form['gender'])
        customer_type = int(request.form['customer_type'])
        type_of_travel = int(request.form['type_of_travel'])
        class_eco=1
        class_ecoplus=int(request.form['class_ecoplus'])
            
        
        unseen_data = [[age, flight_distance, inflight_entertainment, baggage_handling, cleanliness, departure_delay, arrival_delay, gender, customer_type, type_of_travel, class_eco,class_ecoplus]]
        dt={1:'satisfied',0:'dissatisfied'}
        prediction = model.predict(unseen_data)[0]
        return str(dt[prediction])

if __name__ == '__main__':
    app.run(debug=True)
