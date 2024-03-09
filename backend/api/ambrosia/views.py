from rest_framework import  viewsets

from api.ambrosia.models import Recipe, Unit, Ingredient, RecipeIngredient
from api.ambrosia.serializers import RecipeSerializer, UnitSerializer, IngredientSerializer, RecipeIngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recipes to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Units to be viewed or edited.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ingredients to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

