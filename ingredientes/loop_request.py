import json, requests, os
import time

url = "http://localhost:8000/api/ingredients"

json_files = os.listdir("data_csv")

for file in json_files:

    with open("data_csv/"+file, "r") as f:
        ingredients = json.load(f)

    for ingredient in ingredients:
        print(ingredient)
        response = requests.post(url, json=ingredient)

        print(response.status_code)
        print(response.text)
        if response.status_code != 201:
            print("Error")
            exit()