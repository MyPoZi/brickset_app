from django.conf.urls import url
from django.contrib.auth.urls import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'accounts'

urlpatterns = [
    # path(r'^$', views.index, name='index'),
    # path(r'^login$', auth_views.auth_login, {'templates': 'accounts/login'}, name='login'),
    # path(r'^logout$', auth_views.auth_logout, name='logout'),
    # path('login/', TemplateView.as_view(template_name='accounts/login.html')),
    path('', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
