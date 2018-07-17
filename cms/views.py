import django_filters
from django.http import HttpResponse
from rest_framework import viewsets
from django.shortcuts import render

from .models import Shop, Food
from .serializer import ShopSerializer, FoodSerializer

from rest_framework.filters import SearchFilter, OrderingFilter

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [SearchFilter]
    search_fields = ('category','shopname')
    #URLのあとに?search=居酒屋　などと入力して検索


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_fields = ('shop',)

def View(request):
    return render(request, 'cms/html/foodmap.html')# これを使って表示する　リンク先はtemplatesの中
