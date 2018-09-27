from django.conf.urls import url
from . import views

# ルーティンの設定

urlpatterns = [

    # itemの一覧
    url('', views.index, name='index'),

    # itemの更新
    url(r'^(?P<item_id>[0-9]+)/edit/$', views.edit, name='item_edit'),

    # itemの削除
    url(r'^(?P<item_id>[0-9]+)/edit/$', views.delete, name='item_delete'),

    # 欲しいものリストへの追加
    url(r'^(?P<item_id>[0-9]+)/add/wish_list/$', views.add_to_wish_list, name='item_add_wish_list'),

    # 欲しいものリストからの削除
    url(r'^(?P<item_id>[0-9]+)/delete/wish_list/$', views.delete_from_wish_list, name='item_delete_wish_list'),

    # 欲しいものリストの一覧
    url(r'^wish_list/$', views.wish_list_index, name='wish_list_index'),

    url(r'^hello/$', views.hello, name='hello'),

    url(r'^extends/$', views.extends, name='extends'),

    # /post/以下に数字が渡された場合にマッチ
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    # /news/以下に文字列が渡された場合にマッチ
    url(r'^news/(?P<slug>[-\w]+)/$', views.news, name='news'),
]
