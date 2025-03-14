# weather/urls.py
from django.urls import path
from . import views


urlpatterns = [
    # path('weather/', views.GetWeatherView, name='weather-list'), 
    path('favorite_cities/', views.GetCitiesFavorites, name='cities-list'), 

]
