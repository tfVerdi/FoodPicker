from django.contrib import admin
from django.db import models
from logic.models import Ingredient, IngredientCategory, Meal, MealCategory

admin.site.register(Ingredient, on_delete=models.CASCADE)
admin.site.register(IngredientCategory, on_delete=models.CASCADE)
admin.site.register(Meal, on_delete=models.CASCADE)
admin.site.register(MealCategory, on_delete=models.CASCADE)