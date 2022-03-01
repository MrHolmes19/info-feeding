from django.shortcuts import render
from api.serializers import IngredientSerializer, FoodSerializer
from api.utils import filterIngredients, filterFood, ingredientsSummarize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredient, Food

# Create your views here.
class IngredientView(APIView):

    def get(self, request):

        ingredients = Ingredient.objects.all()

        ingredients = filterIngredients(request, ingredients)
        print(len(ingredients))

        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = request.data

        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
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

class IngredientBulkView(APIView):

    def post(self, request):

        data = "" # poner aca funcion para leer csv con todos los ingredientes y meterlos a la bd

        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodView(APIView):

    def get(self, request):

        foods = Food.objects.all()

        foods = filterFood(request, foods)
        print(len(foods))

        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = request.data

        if "ingredients" in data and "subfoods" in data:
            return Response({"message": "you should send ingredients or subfoods"}, status=status.HTTP_400_BAD_REQUEST)

        if "ingredients" in data:
            ingredients = ingredientsSummarize(data["ingredients"])
            print(ingredients)
            return Response(status=status.HTTP_200_OK)
        elif "subfoods" in data:
            print("subfood")
        else:
            return Response({"message": "you should send ingredients or subfoods"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FoodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodDetailView(APIView):

    def get(self, request, pk):

        try:
            food = food.objects.get(pk=pk)
        except food.DoesNotExist:
            return Response({"message": "food not found"}, status=404)

        

        serializer = FoodSerializer(food)
        return Response(serializer.data)
            
    
    def patch(self, request, pk):

        try:
            food = Food.objects.get(pk=pk)
        except food.DoesNotExist:
            return Response({"message": "food not found"}, status=404)
        
        serializer = FoodSerializer(food, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):

        try:
            food = food.objects.get(pk=pk)
        except food.DoesNotExist:
            return Response({"message": "food not found"}, status=404)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)