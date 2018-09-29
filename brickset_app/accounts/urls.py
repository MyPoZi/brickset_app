from django.urls import path


from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create, name='create'),
]
