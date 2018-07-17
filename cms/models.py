from django.db import models


# Create your models here.

class Shop(models.Model):
    shopname = models.CharField('店名', max_length=255, default=1)
    address = models.CharField('住所', max_length=255, blank=True)
    open = models.CharField('オープン日', max_length=255, blank=True)
    category = models.CharField('カテゴリ', max_length=255, blank=True)
    lat = models.CharField('緯度', max_length=255, default=0)
    lng = models.CharField('経度', max_length=255, default=0)
    rate = models.CharField('評価', max_length=255, default=0)
    open_val = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.shopname


class Food(models.Model):
    shop = models.ForeignKey(Shop, verbose_name='店舗', related_name='food_shop', default=1)
    name = models.CharField('料理名', max_length=255, default=1)
    price = models.IntegerField('価格', blank=True, default=1)
    birth_val = models.IntegerField(blank=True, default=1)
    only_val = models.IntegerField(blank=True, default=1)
    popular_val = models.IntegerField(blank=True, default=1)
    url = models.CharField('url', max_length=2000, default="test")

    def __str__(self):
        return self.name


class Review(models.Model):
    shop = models.ForeignKey(Shop, verbose_name='店舗', related_name='review_shop', default=1)
    review = models.CharField('レビュー', max_length=8000, default=1)

    def __str__(self):
        return self.review
