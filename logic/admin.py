from django.contrib import admin
from django.db import models
from logic.models import Ingredient, IngredientCategory, Meal, MealCategory

class IngredientInline(admin.TabularInline):
    model = Ingredient

class IngredientCategoryAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline,
    ]

admin.site.register(Ingredient, on_delete=models.DO_NOTHING)
admin.site.register(IngredientCategory, IngredientCategoryAdmin, on_delete=models.DO_NOTHING)
admin.site.register(Meal, on_delete=models.DO_NOTHING)
admin.site.register(MealCategory, on_delete=models.DO_NOTHING)