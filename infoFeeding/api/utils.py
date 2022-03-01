from .models import Ingredient
from .serializers import IngredientSerializer

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

def filterFood(request, ingredients):
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

conversion = {
    "kg": 1000
}


def ingredientsSummarize(ingredients):

    serialized_ingredients = []
    amounts = []
    for ingredient in ingredients:
        full_ingredient = Ingredient.objects.get(pk=ingredient["id"])
        unit = ingredient["unit"]

        if unit == "Kg":
            amount_in_gr = float(ingredient["amount"]) * 1000
        else:
            amount_in_gr = ingredient["amount"] * conversion[unit] * full_ingredient.density

        serialized = IngredientSerializer(full_ingredient).data

        del serialized["id"]
        serialized_ingredients.append(serialized)
        amounts.append(amount_in_gr)

    total_nutrients = {}
    for i, ing in enumerate(serialized_ingredients):
        for k in ing.keys():
            if type(ing[k]) in [int, float]:
                print(f"{k} voy a sumar: {type(total_nutrients.get(k, 0))} + {type(ing[k])}*{type(amounts[i])}")
                total_nutrients[k] = total_nutrients.get(k, 0) + (float(ing[k])* amounts[i] / 100)
            else:
                print(f"no paso {k}")

    return total_nutrients
        
