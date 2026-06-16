from django.contrib import admin
from logic.models import Ingredient, IngredientCategory, Meal, MealCategory

admin.site.register(Ingredient)
admin.site.register(IngredientCategory)
admin.site.register(Meal)
admin.site.register(MealCategory)