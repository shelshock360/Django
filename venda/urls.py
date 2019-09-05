
from django.urls import path, reverse_lazy
# importar as views de inserir, atualizar e excluir
from .views import ProdutoListCarrinhoVenda
from .views import ProdutoCreateCarrinhoVenda
from .views import ProdutoUpdateCarrinhoVenda
from .views import ProdutoDeleteCarrinhoVenda


urlpatterns = [
    
    path('vender/produtos/', ProdutoListCarrinhoVenda.as_view(), name="lista-vender-produtos"),
    path('cadastrar/produtos/', ProdutoCreateCarrinhoVenda.as_view(), name="cadastrar-carrinhoVenda"),
   	path('editar/produtos/<int:pk>/', ProdutoUpdateCarrinhoVenda.as_view(), name="editar-carrinhoVenda"),
    path('excluir/produtos/<int:pk>/', ProdutoDeleteCarrinhoVenda.as_view(), name="excluir-carrinhoVenda"),
    
]
