from django.shortcuts import render
from .models import Meal, Ingredient

# Create your views here.
def dashboard(response):
    return render(
        response,
        "dashboard/index.html",
        {"ingredients": Ingredient.objects.all}
    )