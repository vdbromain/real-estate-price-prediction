from flask import Flask
from flask import request
from flask import render_template
import json

# Personnal functions
from preprocessing.cleaning_data import preprocessing
from predict.prediction import predict
from receiving_data.processing_request import processing_request

app = Flask(__name__)

# Test if the server is alive and launch the prediction page
@app.route("/", methods=["GET"])
def alive():
    if request.args.get:
        return render_template("prediction.html")


@app.route("/receiving_data", methods=["POST", "GET"])
def receiving_data():
    # processing the data received from the "post request"
    values: dict = processing_request()
    # Converting my dict into a json format as asked in the readme file of the project
    json_data: json = json.dumps(values, indent=8)
    # Shaping the data for them to enter in the model
    preprocess_data: list = preprocessing(json_data)
    # Entering the data in the model and receiving the predicted_price
    predicted_price: float = predict(preprocess_data)
    # Taking only the content of the np.array and rounding it to be more readable
    predicted_price: float = predicted_price[0].round(2)
    # loading the result html page with different variables to resume the question of the user in the final page
    return render_template(
        "result.html",
        prediction=predicted_price,
        province=values["province"],
        nb_rooms=values["nb_rooms"],
        living_area=values["living_area"],
    )


if __name__ == "__main__":
    # Running the app on port 5000, in debugging mode (interactive terminal) and most important thing the host here and not in the Dockerfile !!!
    app.run(port=5000, debug=True, host="0.0.0.0")
