from django.urls import path
from . import views

app_name = 'pessoas'
urlpatterns = [
    path('', views.home, name='home'),
    path('nova', views.nova, name='nova'),
]
