from rest_framework import serializers

from .models import Shop, Food


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'shopname', 'address', 'open', 'category', 'lat', 'lng')


class FoodSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    class Meta:
        model = Food
        fields = ('id', 'name', 'price', 'shop')
