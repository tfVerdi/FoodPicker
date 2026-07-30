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
    name = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(IngredientCategory, on_delete=models.DO_NOTHING, null=True)
    def __str__(self):
        if not self.category:
            return str()
        return f'{IngredientCategory.objects.get(pk=self.category.pk).name} - {self.name}'

class Meal(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True)
    instructions = models.CharField(max_length=2048, null=True)
    category = models.ForeignKey(MealCategory, on_delete=models.DO_NOTHING, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="meal_ingredients")
    optional_ingredients = models.ManyToManyField(Ingredient, blank=True)
    def __str__(self):
        return self.name