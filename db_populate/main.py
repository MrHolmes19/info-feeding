import json
from collections import namedtuple

import pandas as pd
import numpy as np
import os

Pair = namedtuple("Pair", "old new")

pairs = [
    Pair("Alimento", "old_name"),
    Pair("ingredient name", "name"),
    Pair("unit weight", "unit_weight"),
    Pair("allowed units", "allowed_units"),
    Pair("edible pct", "edible_pct"),
    Pair("Energía", "calories"),
    Pair("Agua", "water"),
    Pair("Proteínas", "proteins"),
    Pair("Grasa Total", "total_fats"),
    Pair("Carbohidratos totales", "total_carbohydrates"),
    Pair("Sodio", "sodium"),
    Pair("Potasio", "potassium"),
    Pair("Calcio", "calcium"),
    Pair("Fósforo", "phosphorus"),
    Pair("Hierro", "iron"),
    Pair("Zinc", "zinc"),
    Pair("Tiamina", "vitamin_b1"),
    Pair("Rivoflavina", "vitamin_b2"),
    Pair("Niacina", "vitamin_b3"),
    Pair("Vitamina C", "vitamin_c"),
    Pair("Fibra dietética", "fiber"),
]

def convert_colums(columns, pairs):

    for pair in pairs:
        if pair.old in columns:
            columns[columns.index(pair.old)] = pair.new

    return columns

def xls_to_json(filename):

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = pd.DataFrame(pd.read_excel("data/"+filename)) # , engine='openpyxl'

    columns = df.iloc[1]

    column_header = [f"{columns[i]}" for i in range(len(columns))]
    column_header = list(map(lambda x: x.replace("(nan)", ""), column_header))

    transformed_columns = convert_colums(column_header, pairs)

    df.columns = transformed_columns

    # encuentro los campos que no tienen 'Nº' y los saco de dt
    # empty = df[df[df.columns[0]].isnull()]
    # empty_indexes = empty.index.values.tolist()
    # df = df.drop(labels=empty_indexes, axis=0).drop(labels=3, axis=0)
    df = df.iloc[3:]

    if "Género - especie - variedad" in transformed_columns:
        df.drop("Género - especie - variedad", inplace=True, axis=1)
    #df.drop("nan", inplace=True, axis=1)
    df = df.where(df.notnull(), None)

    #df.to_csv("data_csv/"+filename.replace(".xls", ".csv"), encoding="utf-8")

    ing_dir = df.to_dict(orient='records')

    with open("data_json/"+filename.replace(".xls", ".json"), "w", encoding="utf-8") as f:
        json.dump(ing_dir, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(os.path.join(current_dir))
    xls_file_list = os.listdir('data')

    for xls_file in xls_file_list:
        try:
            xls_to_json(xls_file)
        except:
            print("Error al convertir")
            print(xls_file)
            raise
