from django.conf.urls import url
from django.contrib.auth.urls import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
