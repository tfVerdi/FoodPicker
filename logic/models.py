from django.db import models

class Ingredient(models.Model):
    def __init__(self):
        name = models.CharField(max_length=64)
        category = models.ForeignKey(IngredientCategory)
    def __str__(self):
        return self.name

class Meal(models.Model):
    def __init__(self):
        name = models.CharField(max_length=64)
        description = models.CharField(max_length=256)
        instructions = models.CharField(max_length=2048)
        category = models.ForeignKey(MealCategory)
        ingredients = models.ManyToManyField(Ingredient)
        optional_ingredients = models.ManyToManyField(Ingredient)
    def __str__(self):
        return self.name

class IngredientCategory(models.Model):
    def __init__(self):
        name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class MealCategory(models.Model):
    def __init__(self):
        name = models.CharField(max_length=64)
    def __str__(self):
        return self.name