import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None
__area=None

def get_estimated_price(location,area,sqft,balcony,bath,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    try:
        area_index = __data_columns.index(area.lower())
    except:
        area_index = -1


    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2]=balcony
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    if area_index >= 0:
        x[area_index] = 1


    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations
    global __area

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:len(__data_columns)-3]  # first 3 columns are sqft, bath, bhk
        __area=__data_columns[len(__data_columns)-3:]

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations
def get_area_names():
    return __area

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_area_names())
    # print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other loc