from django.db.models import Sum

from recipes.models import IngredientInRecipe


def generate_shopping_list(user):
    ingredients = IngredientInRecipe.objects.filter(
        recipe__in_shopping_cart__user=user
    ).values(
        'ingredient__name',
        'ingredient__measurement_unit'
    ).annotate(
        total_amount=Sum('amount')
    ).order_by('ingredient__name')

    shopping_list = []
    for ingredient in ingredients:
        name = ingredient['ingredient__name']
        measurement_unit = ingredient['ingredient__measurement_unit']
        amount = ingredient['total_amount']
        shopping_list.append(
            f"{name} ({measurement_unit}) — {amount}"
        )

    return '\n'.join(shopping_list)


def add_recipe_to_collection(model, user, recipe):
    if model.objects.filter(user=user, recipe=recipe).exists():
        return None
    return model.objects.create(user=user, recipe=recipe)


def remove_recipe_from_collection(model, user, recipe):
    obj = model.objects.filter(user=user, recipe=recipe)
    if obj.exists():
        obj.delete()
        return True
    return False

