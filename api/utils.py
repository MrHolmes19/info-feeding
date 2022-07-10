from logging import raiseExceptions
#from numpy import NaN
from .models import Ingredient, Food
from .serializers import IngredientSerializer, FoodSerializer
from rest_framework.exceptions	import APIException, NotFound, ValidationError

class CustomErrors(APIException):
  status_code = 404
  default_detail = "Something happen here, look out you moron"
  


def filterIngredients(request, ingredients):
  '''
  This function matches properties objects with query params filter in url as: 
        * containing name (string)
        * prices greater/lesser or equals than (int or float)
  - receives: request
  - returns: queryset with filtered objects. If not receive query params, return all.
  '''
  
  name = request.query_params.get('name')

  group = request.query_params.get('group')
  subgroup = request.query_params.get('subgroup')
  origin = request.query_params.get('origin')
  commercial_section = request.query_params.get('commercial_section')

  if name:
    ingredients = ingredients.filter(name__contains = name)
  if group:
    ingredients = ingredients.filter(group = group)
  if subgroup:
    ingredients = ingredients.filter(subgroup = subgroup)
  if origin:
    ingredients = ingredients.filter(origin = origin)
  if commercial_section:
    ingredients = ingredients.filter(commercial_section = commercial_section)
    
  return ingredients

def filterFood(request, foods):
  '''
  This function matches properties objects with query params filter in url as: 
        * containing name (string)
        * prices greater/lesser or equals than (int or float)
  - receives: request
  - returns: queryset with filtered objects. If not receive query params, return all.
  '''  
  name = request.query_params.get('name')

  group = request.query_params.get('group')
  subgroup = request.query_params.get('subgroup')
  origin = request.query_params.get('origin')
  commercial_section = request.query_params.get('commercial_section')

  if name:
    foods = foods.filter(name__contains = name)
  if group:
    foods = foods.filter(group = group)
  if subgroup:
    foods = foods.filter(subgroup = subgroup)
  if origin:
    foods = foods.filter(origin = origin)
  if commercial_section:
    foods = foods.filter(commercial_section = commercial_section)
    
  return foods

# Esto lo vamos separar en un archivo para que sirva para traerlo y ademas para que popule tablas Unit

# mililiters equivalent
conversion = {
    "ml": 1,
    "cm3": 1,
    "lts": 1000,
    "cuchara té": 5,
    "cuchara postre": 15,
    "cuchara sopera": 30,
    "vaso": 200,
    "taza": 250,
}


def ingredientsSummarize(ingredients):
    '''
    Sum all nutrients of each ingredient involved
    Receives: ingredients from data object (list of dicts)
    Returns: nutrients of the food (dict)
    '''
    print("ingredients que recibe: ", ingredients)
    serialized_ingredients = []
    amounts = []
    
    for ingredient in ingredients:
        try:
            ingredient_info = Ingredient.objects.get(pk=ingredient["id"])
        except Ingredient.DoesNotExist:
            raise NotFound(detail="One or more ingredients were not found")
        except Exception:
            # handling unexpected error
            raise
        
        amount = ingredient['amount']  
        if str(amount).isnumeric() and float(amount)>0:
            amount = float(amount)
        else:
            raise ValidationError(detail = {"detail": "amount must be an int or a float greater than 0"})
    
        unit = ingredient["unit"]

        if unit == 'g':
            amount_in_gr = amount
        elif unit == "kg":
            amount_in_gr = amount * 1000
        elif unit == "unidades":
            amount_in_gr = amount * ingredient_info.unit_weight
        elif unit in conversion.keys():
            amount_in_gr = amount * conversion[unit] * ingredient_info.density
        else:
            raise NotFound(detail="Unit is not allowed or was not sent")

        serialized = IngredientSerializer(ingredient_info).data

        del serialized["id"]
        serialized_ingredients.append(serialized)
        amounts.append(amount_in_gr)

    total_nutrients = {}
    for i, ing in enumerate(serialized_ingredients):
        for k in ing.keys():
            if type(ing[k]) in [int, float]:

                #print(f"{k} voy a sumar: {type(total_nutrients.get(k, 0))} + {type(ing[k])}*{type(amounts[i])}")
                total_nutrients[k] = round(total_nutrients.get(k, 0) + (float(ing[k])* amounts[i] * float(ing["edible_ptc"]) / 100),2)
                ## AGREGAR MULTIPLICACION POR EDIBLE_PTC
            #else:
                #print(f"no pasó {k}")
    
    del total_nutrients["edible_ptc"]
    return total_nutrients
        

def subfoodsSummarize(subfoods):
    '''
    Sum all nutrients of each subfood involved
    Receives: ingredients from data object (list of dicts)
    Returns: nutrients of the food (dict)
    '''
    serialized_subfoods = []
    subfood_portions = []
    
    for subfood in subfoods:
        
        try:
            subfood_info = Food.objects.get(pk=subfood["id"])
        except:
            raise NotFound(detail="one or more subfoods were not found")
        
        try:
            portions = subfood["portions"]
        except:
            raise NotFound(detail="You should specify how many portions you take from a subfood")

        serialized = FoodSerializer(subfood_info).data
        del serialized["id"]
        
        serialized_subfoods.append(serialized)
        subfood_portions.append(portions)

    total_nutrients = {}
    for i, sf in enumerate(serialized_subfoods):
        for k in sf.keys():
            if type(sf[k]) in [int, float]:
                #print(f"{k} voy a sumar: {type(total_nutrients.get(k, 0))} + {type(sf[k])}*{type(amounts[i])}")
                total_nutrients[k] = round(total_nutrients.get(k, 0) + (float(sf[k]) * subfood_portions[i]/sf['portions']),2)
                ## AGREGAR MULTIPLICACION POR EDIBLE_PTC
            #else:
                #print(f"no pasó {k}")
    
    del total_nutrients["portions"]
    print("total_nutrientes: ", total_nutrients)
    
    return total_nutrients


def group_by_name(data):
    """
    returns a list with no repeated names, with its posible units and presentations
    """
    data_result = []
    for ing in data:
        ## Checking if ingredient was already stored
        ing_exist = False
        for stored_ing in data_result:
            if ing["name"] in stored_ing["name"]:
                ing_exist = True
                break
        ## Defines presentation info about this ingredient
        presentation = {          
            "presentation": ing["presentation"],
            "unit_weight": ing["unit_weight"],
            "allowed_units": ing["allowed_units"].split(",") if ing["allowed_units"] else None # TODO: Change this
        }
        ## If ingredient is new, append ingredient and its presentation
        if not ing_exist:
            ing_result = {
                "name": ing["name"],
                "presentations": [presentation]
            }
            data_result.append(ing_result)
        else:
            ## Check if this presentation was already stored in the ingredient (come repeated cause of cooking condition)
            existing_ing = list(filter(lambda x: x["name"]==ing["name"], data_result))[0]
            pres_exist = False
            for pres in existing_ing["presentations"]:
                if presentation["presentation"] == pres["presentation"]:
                    pres_exist = True
            ## If presentation is new, append to presentation list
            if not pres_exist:
                existing_ing["presentations"].append(presentation)
                    
    return data_result