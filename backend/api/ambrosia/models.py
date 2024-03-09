from django.db import models



class Unit(models.Model):

    name = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )

    abbreviation = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )


class Ingredient(models.Model):

    name = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )


class Recipe(models.Model):
    name = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )

    steps = models.TextField(
        blank=False,
        null=False
    )

    duration = models.IntegerField(
        null=True
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient'
    )

    # TODO: categories, pictures, amount of people


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=False
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        null=False
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        null=True
    )

    amount = models.FloatField(
        null=True
    )

