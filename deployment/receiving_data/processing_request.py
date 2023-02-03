from flask import request

# Processing our post request
def processing_request() -> dict:
    if request.method == "POST":
        # Defining a dictionnary to store the data from the form
        values: dict = {}
        values["province"] = request.form["Province"]
        values["nb_rooms"] = request.form["nb_rooms"]
        values["living_area"] = request.form["living_area"]
        values["open_fire"] = request.form["open_fire"]
        values["terrace"] = request.form["terrace"]
        values["garden"] = request.form["garden"]
        values["swimming_pool"] = request.form["swimming_pool"]
        values["state"] = request.form["state"]
    return values
