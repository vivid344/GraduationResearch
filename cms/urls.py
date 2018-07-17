from rest_framework import routers
from .views import ShopViewSet, FoodViewSet
from django.conf.urls import url
from cms import views


router = routers.DefaultRouter()
router.register(r'Shops', ShopViewSet)
router.register(r'Foods', FoodViewSet)

urlpatterns = [
    url(r'', views.View, name='View'),
]