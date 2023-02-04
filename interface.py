from flask import Flask, render_template , request
import numpy as np
from utils import CarPrice
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/valuation' , methods = ['POST','GET'])
def valuation():
    if request.method == 'POST':
        data = request.form.get
        
        Name = data('Name')
        Location = data('Location')
        Age = eval(data('Age'))
        Kilometers_Driven = eval(data('Kilometers_Driven'))
        Fuel_Type = data('Fuel_Type')
        Transmission = data('Transmission')
        Owner_Type = data('Owner_Type')
        Mileage = eval(data('Mileage'))
        Engine = eval(data('Engine'))
        Power =eval(data('Power'))
        Seats = int(data('Seats'))

        CP = CarPrice(Name, Location, Age, Kilometers_Driven, Fuel_Type,
        Transmission, Owner_Type, Mileage,Engine,Power,Seats)
        
        Price = CP.prediction()

        return render_template('index.html' , Predicted_Price = np.around(Price, decimals = 2))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)


