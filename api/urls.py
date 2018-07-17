from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^recommend/$', views.recommend, name='recommend'),  # 一覧
    url(r'^set_up/$', views.set_up, name='set_up'),  # 初期にアクセス
    # url(r'^sql_update/$', views.sql_update, name='aql_update'),  # 初期にアクセス
]
