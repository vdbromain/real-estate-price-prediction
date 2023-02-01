import pickle
import numpy as np

model = pickle.load(open("./model/model.pkl", 'rb'))

def predict(prepro_data : list) -> float :
    features = [np.array(prepro_data)]
    predicted_price = model.predict(features)

    return predicted_price 