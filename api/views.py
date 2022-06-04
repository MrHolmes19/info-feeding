import json
from django.shortcuts import render
from api.serializers import IngredientSerializer, FoodSerializer
from api.utils import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Ingredient, Food
from pprint import pprint


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    
    def list(self, request):       
        ingredients = filterIngredients(request, self.queryset)
        serializer = self.serializer_class(ingredients, many=True)
        data = group_by_name(serializer.data)
        return Response(data)

class FoodsViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    
    def list(self, request):       
        food = filterFood(request, self.queryset)
        serializer = self.serializer_class(food, many=True)
        return Response(serializer.data)
    

    def create(self, request):
        
        data = request.data

        if "ingredients" in data and "subfoods" in data:
            return Response({"message": "you should send ingredients OR subfoods"}, status=status.HTTP_400_BAD_REQUEST)

        if "ingredients" in data:

            nutrients = ingredientsSummarize(data["ingredients"])
            print("data: ", data)
            print("nutrients: ", nutrients)
            data.update(nutrients)
            data['ingredients'] = json.dumps(data['ingredients'])
        
        elif "subfoods" in data:
            nutrients = subfoodsSummarize(data["subfoods"])
            data.update(nutrients)
            data['subfoods'] = json.dumps(data['subfoods'])
        else:
            return Response({"message": "you should send either ingredients or subfoods"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FoodSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        
        try:
            food = Food.objects.get(pk=pk)
        except food.DoesNotExist:
            return Response({"message": "food not found"}, status=404)

        if not food.ingredients:
            serializer = FoodSerializer(food, data=request.data, partial=True)
        else:
            ingredients = json.loads(food.ingredients)
            nutrients = ingredientsSummarize(ingredients)
            new_data = request.data
            new_data.update(nutrients)
            new_data['ingredients'] = json.dumps(new_data['ingredients'])
            serializer = FoodSerializer(food, data=new_data, partial=True)
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
