from django.urls import path, include
from .api import RegisterAPI, LoginAPI, AccountAPI
from knox import views as knox_views

urlpatterns = [
    path('', include('knox.urls')),
    path('register', RegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('account', AccountAPI.as_view()),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout')
]
