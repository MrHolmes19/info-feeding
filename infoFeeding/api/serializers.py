from .models import Ingredient, Food
from rest_framework import serializers

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'