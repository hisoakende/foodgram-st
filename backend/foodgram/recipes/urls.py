from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.views import (
    IngredientViewSet, RecipeViewSet,
    download_shopping_cart, get_recipe_short_link
)

router = DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path(
        'api/recipes/download_shopping_cart/',
        download_shopping_cart,
        name='download_shopping_cart'
    ),
    path(
        'api/recipes/<int:id>/get-link/',
        get_recipe_short_link,
        name='get_recipe_short_link'
    ),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),
]
