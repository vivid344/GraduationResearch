import json
import time
from time import sleep

import requests
from bs4 import BeautifulSoup
# Create your views here.
from django.http import HttpResponse

from cms.models import Food, Review


def recommend(request):
    if request.method == 'GET':

        price = int(request.GET['price']) if request.GET['price'] != '' else 1000000000
        category = request.GET['category']
        birth = int(request.GET['birth'])
        old_shop = int(request.GET['old_shop'])
        only = int(request.GET['only'])
        popular = int(request.GET['popular'])
        food_list = []

        if price != "":
            if category != "":  # 全部入力されてた場合
                if category == 'レストラン':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND price <= %s AND " +
                        "(category LIKE %s OR category LIKE %s OR category LIKE %s OR " +
                        "category LIKE %s OR category LIKE %s OR category LIKE %s OR " +
                        "category LIKE %s OR category LIKE %s OR category LIKE %s OR " +
                        "category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , [price, "%和食%", "%洋食%", "%中華%", "%アジア%", "%カレー%", "%焼肉%", "%鍋%", "%居酒屋%", "%創作料理%",
                           "%ファミレス%", birth, old_shop, only, popular]
                    )
                elif category == 'ラーメン':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND price <= %s AND " +
                        "(category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , [price, "%ラーメン%", "%つけ麺%", birth, old_shop, only, popular]
                    )
                elif category == 'カフェ・喫茶':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND price <= %s AND " +
                        "(category LIKE %s OR category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , [price, "%カフェ%", "%喫茶%", "%専門店%", birth, old_shop, only, popular]
                    )
                elif category == 'パン・スイーツ':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND price <= %s AND " +
                        "(category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , [price, "%パン%", "%スイーツ%", birth, old_shop, only, popular]
                    )
                elif category == 'バー・お酒':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND price <= %s AND " +
                        "(category LIKE %s OR category LIKE %s OR category LIKE %s OR " +
                        "category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , [price, "バー", "%パブ%", "%ラウンジ%", "%ワインバー%", "%ビア%", birth, old_shop, only, popular]
                    )
                elif category == '旅館・オーベルジュ':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND price <= %s AND " +
                        "(category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , [price, "%旅館%", "%オーベルジュ%", birth, old_shop, only, popular]
                    )
                elif category == 'その他':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND price <= %s AND " +
                        "(category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , [price, "その他", birth, old_shop, only, popular]
                    )

            else:  # カテゴリが入力されてなかった場合
                food = Food.objects.raw(
                    "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                    "where price != 0 AND price <= %s AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                    "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                    , [price, birth, old_shop, only, popular]
                )
        else:
            if category != "":  # 料金が入力されていなかった場合
                if category == 'レストラン':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND " +
                        "(category LIKE %s OR category LIKE %s OR category LIKE %s OR " +
                        "category LIKE %s OR category LIKE %s OR category LIKE %s OR " +
                        "category LIKE %s OR category LIKE %s OR category LIKE %s OR " +
                        "category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , ["%和食%", "%洋食%", "%中華%", "%アジア%", "%カレー%", "%焼肉%", "%鍋%", "%居酒屋%", "%創作料理%",
                           "%ファミレス%", birth, old_shop, only, popular]
                    )
                elif category == 'ラーメン':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND " +
                        "(category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , ["%ラーメン%", "%つけ麺%", birth, old_shop, only, popular]
                    )
                elif category == 'カフェ・喫茶':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND " +
                        "(category LIKE %s OR category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , ["%カフェ%", "%喫茶%", "%専門店%", birth, old_shop, only, popular]
                    )
                elif category == 'パン・スイーツ':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND " +
                        "(category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , ["%パン%", "%スイーツ%", birth, old_shop, only, popular]
                    )
                elif category == 'バー・お酒':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND " +
                        "(category LIKE %s OR category LIKE %s OR category LIKE %s OR " +
                        "category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , ["バー", "%パブ%", "%ラウンジ%", "%ワインバー%", "%ビア%", birth, old_shop, only, popular]
                    )
                elif category == '旅館・オーベルジュ':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND " +
                        "(category LIKE %s OR category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , ["%旅館%", "%オーベルジュ%", birth, old_shop, only, popular]
                    )
                elif category == 'その他':
                    food = Food.objects.raw(
                        "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                        "where price != 0 AND " +
                        "(category LIKE %s) AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                        "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                        , ["その他", birth, old_shop, only, popular]
                    )
            else:
                food = Food.objects.raw(
                    "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
                    "where price != 0 AND (birth_val > 2 OR only_val > 2 OR popular_val > 2)" +
                    "order by (birth_val * %s) + (open_val * %s) + (only_val * %s) + (popular_val * %s) desc LIMIT 8"
                    , [birth, old_shop, only, popular]
                )

        for obj in food:
            res = {
                'shopname': obj.shopname,
                'name': obj.name,
                'lat': obj.lat,
                'lng': obj.lng,
                'id': obj.shop_id,
                'price': obj.price,
                'utility': "{0:.1f}".format(
                    float((obj.birth_val * birth) + (obj.open_val * old_shop) + (obj.only_val * only) + (
                        obj.popular_val * popular)) * 0.1),
                'url': obj.url
            }

            food_list.append(res)

        response = json.dumps(food_list, ensure_ascii=False)
        return HttpResponse(response, content_type='text/javascript')


def set_up(request):
    if request.method == 'GET':
        food = Food.objects.raw(
            "select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id " +
            "where price != 0 " +
            "order by rand() LIMIT 8")

        food_list = []
        for obj in food:
            res = {
                'shopname': obj.shopname,
                'name': obj.name,
                'lat': obj.lat,
                'lng': obj.lng,
                'id': obj.shop_id,
                'price': obj.price,
                'utility': "0",
                'url': obj.url
            }

            food_list.append(res)

        response = json.dumps(food_list, ensure_ascii=False)
        return HttpResponse(response, content_type='text/javascript')


# def sql_update(request):
#     food_object = Food.objects.raw("select * from cms_food inner join cms_shop on cms_food.shop_id = cms_shop.id")
#
#     for food_raw in food_object:
#         if food_raw.url == "https://s.yimg.jp/images/clear.gif":
#             sleep(0.5)
#             url = "https://search.yahoo.co.jp/image/search?p=" + food_raw.name + "%E3%80%80" + food_raw.shopname
#             response = requests.get(url)
#             response.encoding = 'UTF-8'
#             link = BeautifulSoup(response.content, "lxml")
#             img = link.find("img")
#             img_url =img.get("src")
#             food_raw.url = img_url
#             food_raw.save()
#
#     return HttpResponse("0", content_type='text/javascript')
