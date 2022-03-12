import json
from django.shortcuts import render
from api.serializers import IngredientSerializer, FoodSerializer
from api.utils import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredient, Food

# Create your views here.
class IngredientView(APIView):

    def get(self, request):

        ingredients = Ingredient.objects.all()

        ingredients = filterIngredients(request, ingredients)
        #print(len(ingredients))

        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = request.data

        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientDetailView(APIView):

    def get(self, request, pk):

        try:
            ingredient = Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            return Response({"message": "Ingredient not found"}, status=404)
  
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)
            
    
    def patch(self, request, pk):

        try:
            ingredient = Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            return Response({"message": "Ingredient not found"}, status=404)
        
        serializer = IngredientSerializer(ingredient, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):

        try:
            ingredient = Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            return Response({"message": "Ingredient not found"}, status=404)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
'''
class IngredientBulkView(APIView):

    def post(self, request):

        data = "" # poner aca funcion para leer csv con todos los ingredientes y meterlos a la bd

        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class FoodView(APIView):

    def get(self, request):
        
        foods = Food.objects.all()
        foods = filterFood(request, foods)

        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = request.data

        if "ingredients" in data and "subfoods" in data:
            return Response({"message": "you should send ingredients OR subfoods"}, status=status.HTTP_400_BAD_REQUEST)

        if "ingredients" in data:
            nutrients = ingredientsSummarize(data["ingredients"])
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


class FoodDetailView(APIView):

    def get(self, request, pk):

        try:
            food = Food.objects.get(pk=pk)
        except food.DoesNotExist:
            return Response({"message": "food not found"}, status=404)

        serializer = FoodSerializer(food)
        return Response(serializer.data)      
    
    def patch(self, request, pk):

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
    
    def delete(self, request, pk):

        try:
            food = Food.objects.get(pk=pk)
        except food.DoesNotExist:
            return Response({"message": "food not found"}, status=404)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)