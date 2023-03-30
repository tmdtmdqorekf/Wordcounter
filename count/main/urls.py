from django.urls import path
from main.views import main, result

urlpatterns = [
    path('', main, name='main'),
    path('result/', result, name='result'),
]