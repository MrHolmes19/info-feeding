from .models import Ingredient
from rest_framework import serializers

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'