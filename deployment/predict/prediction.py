import pickle
import numpy as np

# Loading the model's file
model = pickle.load(open("./model/model.pkl", "rb"))


def predict(prepro_data: list) -> float:
    # Shaping the prepro_data in np.array for them to fit in the shape the model needs
    features = [np.array(prepro_data)]
    predicted_price = model.predict(features)

    return predicted_price
