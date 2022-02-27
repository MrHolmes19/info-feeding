from django.urls import path
from .views import *

urlpatterns = [
    path('ingredients', IngredientView.as_view()),
]
