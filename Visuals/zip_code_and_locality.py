import os
import re
import requests
import json

from bs4 import BeautifulSoup



filename = "./data/10289835.html"

with open(filename, "r") as my_file :
    my_file = my_file.read()
    soup = BeautifulSoup(my_file, "html.parser")

    td = soup.find_all("td")

    th = soup.find_all("th")

    locality = soup.find_all("span", attrs={"class": "classified__information--address-row"})
    subtype_property = soup.find_all("h1",attrs={"class": "classified__title"})

    for elem in locality :
        pattern = "([0-9]{4})"
        elem_text = elem.text
        if re.findall(pattern, elem_text) :
            zip_code = re.findall(pattern, elem_text)
            zip_code_str = zip_code[0]

    for elem in subtype_property :
        elem_text = elem.text
        elem_text = elem_text.replace(" ","").replace("\n","")

        if elem_text.find("louer"):
            index_a = elem_text.find("à")
            type = elem_text[:index_a]
            
        elif elem_text.find("vendre"):
            index_vendre = elem_text.find("à")
            type = elem_text[:index_a]    


    print(zip_code_str)
    print(type)




    
    #td_content = [i.text for i in td]

    #print(td_content)