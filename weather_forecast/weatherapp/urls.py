from django.urls import path
from .views import WeatherApi

urlpatterns = [
    path('v1/forecast', WeatherApi.as_view(), name='forecast-api')
]