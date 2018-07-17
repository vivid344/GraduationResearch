from django.contrib import admin
from cms.models import Shop, Food


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'shopname', 'address', 'open', 'category', 'lat', 'lng')  # 一覧に出したい項目
    list_display_links = ('id', 'shopname',)  # 修正リンクでクリックできる項目

admin.site.register(Shop, ShopAdmin) #上でクラスを定義して，ShopにはShopAdinを表示させるという宣言


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目

admin.site.register(Food, FoodAdmin)

# Register your models here.
