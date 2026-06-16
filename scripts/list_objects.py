import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FoodPicker.settings")
django.setup()
from logic.models import Ingredient, IngredientCategory, Meal, MealCategory

print(Ingredient.objects.all())
print(IngredientCategory.objects.all())
print(Meal.objects.all())
print(MealCategory.objects.all())