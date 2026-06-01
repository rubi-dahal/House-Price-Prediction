import json
import pickle
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    input_x = np.zeros(len(__data_columns))
    input_x[0] = sqft
    input_x[1] = bath
    input_x[2] = bhk

    if loc_index >= 0:
        input_x[loc_index] = 1

    return round(__model.predict([input_x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts... Start")
    global __data_columns
    global __locations
    global __model          

    with open("./artifacts/columns.json", 'r', encoding='utf-8', errors='ignore') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("Loading artifacts done!")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Block Jayanagar',1000,2,2))
    print(get_estimated_price('Banaswadi',1000,2,3))
    print(get_estimated_price('Badavala Nagar',1000,3,2))
    print(get_estimated_price('Banaswadi',1000,2,2))