import numpy as np
import json

from flask import redirect, url_for

def preprocessing(data : str ) -> list :
    #convert the json data received in a dict
    data_dict = json.loads(data)

    #create a list with 23 elements who will be the prepro_data
    prepro_data = [0 for x in range(23)]

    #print(prepro_data)

    #Go trough the whole dict to check the values the user gives us
    for k, v in data_dict.items() :
        #print(f"k = {k}")
        #print(f"v = {v}")
        if k == "province":
            if v == "":
                print("I go into the condition")
                #should ask the user to give us a province
                redirect(url_for('error', error = "Would you mind give me a province ?"))
            elif v == "Anvers":
                prepro_data[6] = 1
            elif v == "Brabant flamand":
                prepro_data[7] = 1
            elif v == "Brabant wallon":
                prepro_data[8] = 1
            elif v == "Bruxelles" :
                prepro_data[9] = 1
            elif v == "Flandre occidentale":
                prepro_data[10] = 1
            elif v == "Flandre orientale":
                prepro_data[11] = 1
            elif v == "Hainaut":
                prepro_data[12] = 1
            elif v == "Liege":
                prepro_data[13] = 1
            elif v == "Limbourg":
                prepro_data[14] = 1
            elif v == "Luxembourg":
                prepro_data[15] = 1
            elif v == "Namur" :
                prepro_data[16] = 1
            else :
                raise NameError('There is a problem with the province')
        if k == "nb_rooms":
            if int(v) > 0 :
                prepro_data[0] = v
            else :
                #should ask the user to give us a living area
                redirect(url_for('error', error = "Would you mind give me a number of rooms greater than zero ?"))
                
        if k == "living_area":
            if int(v) > 0 :
                prepro_data[1] = v
            else :
                #should ask the user to give us a living area
                redirect(url_for('error', error = "Would you mind give me a living area greater than zero ?"))
        if k == "open_fire":
            prepro_data[2] = v
        if k == "terrace":
            prepro_data[3] = v
        if k == "garden":
            prepro_data[4] = v
        if k == "swimming_pool":
            prepro_data[5] = v
        if k == "state":
            if int(v) == 0 :
                prepro_data[17] = 1
            elif v == 1 :
                prepro_data[18] = 1
            elif v == 2 :
                prepro_data[19] = 1
            elif v == 3 :
                prepro_data[20] = 1
            elif v == 4 :
                prepro_data[21] = 1
            elif v == 5 :
                prepro_data[22] = 1
                
    return prepro_data
