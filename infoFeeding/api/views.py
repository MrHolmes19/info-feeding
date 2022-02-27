from django.shortcuts import render
from api.serializers import IngredientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredient

# Create your views here.
class IngredientView(APIView):

    def get(self, request):

        ingredients = Ingredient.objects.all()

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

class IngredientBulkView(APIView):

    def post(self, request):

        data = "" # poner aca funcion para leer csv con todos los ingredientes y meterlos a la bd

        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
