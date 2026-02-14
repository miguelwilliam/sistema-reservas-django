from django.urls import path
from . import views

app_name = 'itens'
urlpatterns = [
    path('', views.home, name='home'),
    path('novo-item', views.novo_item, name='novo-item'),
    path('nova-categoria', views.nova_categoria, name='nova-categoria'),
]
