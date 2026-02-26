from django.contrib import admin
from django.urls import path
from . import views

app_name = 'emprestimos'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('novo/', views.novo, name='novo'),
    path('apagar/<int:id>', views.apagar, name='apagar')
]
