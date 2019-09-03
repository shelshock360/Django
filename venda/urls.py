
from django.urls import path, reverse_lazy
# importar as views de inserir, atualizar e excluir
from .views import ProdutoListCarrinhoVenda

urlpatterns = [
    
    path('vender/produtos/', ProdutoListCarrinhoVenda.as_view(), name="lista-vender-produtos"),

]
