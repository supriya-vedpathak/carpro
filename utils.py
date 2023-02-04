import pandas as pd
import numpy as np
import json
import pickle

class CarPrice():
    def __init__(self , Name, Location, Age, Kilometers_Driven, Fuel_Type,
     Transmission, Owner_Type, Mileage,Engine,Power,Seats):
        self.Name = Name
        self.Location = Location
        self.Age = Age
        self.Kilometers_Driven = Kilometers_Driven
        self.Fuel_Type = Fuel_Type
        self.Transmission = Transmission
        self.Owner_Type = Owner_Type
        self.Mileage = Mileage
        self.Engine = Engine
        self.Power = Power
        self.Seats = Seats

    def import_models(self):
        with open('linreg.pkl' , 'rb') as f:
            self.linreg  = pickle.load(f)

        with open('column_data.json', 'r') as f:
            self.column_data = json.load(f)

    def prediction(self):
        self.import_models()
        
        tesry = np.zeros(self.linreg.n_features_in_)

        tesry[0] = self.Age
        tesry[1] = self.Kilometers_Driven
        tesry[2] = self.column_data['Fuel_Type'][self.Fuel_Type]
        tesry[3] = self.column_data['Transmission'][self.Transmission]
        tesry[4] = self.column_data['Owner_Type'][self.Owner_Type]
        tesry[5] = self.Mileage
        tesry[6] = self.Engine
        tesry[7] = self.Power
        tesry[8] = self.Seats

        n_index =  self.column_data["Column_Names"].index('Name_'+ self.Name)
        tesry[n_index] = 1
        
        l_index = self.column_data["Column_Names"].index('Location_'+ self.Location)
        tesry[l_index] = 1

        price = self.linreg.predict([tesry])

        return price