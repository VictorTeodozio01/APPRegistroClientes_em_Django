from django.urls import path
from .views import listar_clientes, adicionar_cliente, editar_cliente, excluir_cliente

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),
    path('adicionar/', adicionar_cliente, name='adicionar_cliente'),
    path('editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),
]
