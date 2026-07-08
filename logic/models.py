from django.db import models

class IngredientCategory(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
    
class MealCategory(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'{IngredientCategory.objects.get(pk=self.category.pk).name} - {self.name}'

class Meal(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, null=True)
    instructions = models.CharField(max_length=2048, null=True)
    category = models.ForeignKey(MealCategory, on_delete=models.CASCADE, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="meal_ingredients")
    optional_ingredients = models.ManyToManyField(Ingredient)
    def __str__(self):
        return self.name