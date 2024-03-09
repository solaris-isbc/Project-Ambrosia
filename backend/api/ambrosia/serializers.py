from rest_framework import serializers

from api.ambrosia.models import Recipe


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'steps',
            'duration'
        ]
