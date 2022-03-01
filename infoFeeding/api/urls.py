from django.urls import path
from .views import *

urlpatterns = [
    path('ingredients', IngredientView.as_view()),
    path('ingredients/<int:pk>', IngredientDetailView.as_view()),
    path('foods', FoodView.as_view()),
    path('foods/<int:pk>', FoodDetailView.as_view()),
]
