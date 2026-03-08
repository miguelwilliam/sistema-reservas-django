from django.urls import path
from . import views

app_name = 'itens'
urlpatterns = [
    path('', views.home, name='home'),
    path('novo-item/', views.novo_item, name='novo-item'),
    path('nova-categoria/', views.nova_categoria, name='nova-categoria'),
    path('apagar-item/<int:id>/', views.apagar_item, name='apagar-item'),
    path('apagar-categoria/<int:id>/', views.apagar_categoria, name='apagar-categoria'),
    path('editar-item/<int:id>/', views.editar_item, name='editar-item'),
    path('editar-categoria/<int:id>/', views.editar_categoria, name='editar-categoria')
]
