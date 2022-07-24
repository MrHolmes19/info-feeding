import json, requests, os
import time

url = "http://localhost:8000/api/ingredients/"

json_files = os.listdir("data_json")

for file in json_files:
    print("file: ", file)
    with open("data_json/"+file, "r") as f:
        ingredients = json.load(f)

    for ingredient in ingredients:
        response = requests.post(url, json=ingredient)
        print(ingredient, response)
        if response.status_code != 201:
            print(response.status_code)
            print(response.text)
            print(file)
            print("Error")
            exit()