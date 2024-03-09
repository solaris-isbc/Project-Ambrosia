from rest_framework import  viewsets

from api.ambrosia.models import Recipe
from api.ambrosia.serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recipes to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


