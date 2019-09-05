
from django.urls import path, reverse_lazy
# importar as views de inserir, atualizar e excluir
from .views import ProdutoListCarrinhoVenda
from .views import ProdutoCreateCarrinhoVenda
from .views import ProdutoUpdateCarrinhoVenda
from .views import ProdutoDeleteCarrinhoVenda


urlpatterns = [
    
    path('vender/produtos/', ProdutoListCarrinhoVenda.as_view(), name="lista-vender-produtos"),
    path('adicionar/produto/', ProdutoCreateCarrinhoVenda.as_view(), name="cadastrar-produtoCarrinho"),
   	path('atualizar/produto/<int:pk>/', ProdutoUpdateCarrinhoVenda.as_view(), name="editar-produtoCarrinho"),
    path('remover/produto/<int:pk>/', ProdutoDeleteCarrinhoVenda.as_view(), name="excluir-produtoCarrinho"),
    
]
