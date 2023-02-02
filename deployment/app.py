from flask import Flask, redirect, url_for, request, render_template, flash
import json
#spipimport os


#Personnal functions
from preprocessing.cleaning_data import preprocessing
from predict.prediction import predict

app = Flask(__name__)

#Defining the secret_key for the flash function
#secret_key = os.urandom(24).hex()
#app.config['SECRET_KEY'] = secret_key


#Test if the server is alive
@app.route('/', methods=['GET'])
def alive():
    if request.args.get :
        return render_template("prediction.html") 

#Display the error if the data is wrong
@app.route('/error/<error>')
def error(error):
    return error

@app.route('/prediction')
def enter_data():
    return render_template('prediction.html')

@app.route('/receiving_data', methods=['POST', 'GET'])
def receiving_data():
    if request.method == "POST":
        values = {}

        province = request.form['Province']
        #print(f'Province = {province}')
        #if province == "Empty":
        #    flash('Province is required!')
        values['province'] = province
        

        nb_rooms = request.form['nb_rooms']
        values['nb_rooms'] = nb_rooms

        living_area = request.form['living_area']
        values['living_area'] = living_area

        open_fire = request.form['open_fire']
        values['open_fire'] = open_fire

        terrace = request.form['terrace']
        values['terrace'] = terrace

        garden = request.form['garden']
        values['garden'] = garden

        swim_pool = request.form['swimming_pool']
        values['swimming_pool'] = swim_pool

        state = request.form['state']
        values['state'] = state

        json_data = json.dumps(values, indent=8)
        print(json_data)

        preprocess_data = preprocessing(json_data)
        print(preprocess_data)

        predicted_price = predict(preprocess_data)

        predicted_price = predicted_price[0].round(2)
    
        return render_template('result.html', prediction = predicted_price, province = values['province'], nb_rooms = values['nb_rooms'], living_area = values['living_area'])


#GET request returning a string to explain what the POST expect (data and format).   

if __name__ == '__main__' :
    app.run(port=5000, debug=True, host="0.0.0.0")