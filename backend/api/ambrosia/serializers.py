from rest_framework import serializers

from api.ambrosia.models import Recipe, Unit, Ingredient, RecipeIngredient


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = [
            'id',
            'name',
            'abbreviation',
        ]


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
        ]


class RecipeIngredientSerializer(serializers.HyperlinkedModelSerializer):
    unit = UnitSerializer()
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = [
            'id',
            'amount',
            'ingredient',
            'unit',
        ]


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'name',
            'steps',
            'duration',
            'ingredients',
        ]
