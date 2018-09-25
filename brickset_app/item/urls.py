from django.conf.urls import url

from . import views

# ルーティンの設定

urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),

    url(r'^extends/$', views.extends, name='extends'),

    # /post/以下に数字が渡された場合にマッチ
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    # /news/以下に文字列が渡された場合にマッチ
    url(r'^news/(?P<slug>[-\w]+)/$', views.news, name='news'),
]