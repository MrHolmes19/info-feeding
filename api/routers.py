from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'ingredients', IngredientViewSet, basename = 'ingredients')
router.register(r'foods', FoodsViewSet, basename = 'foods')

urlpatterns = router.urls