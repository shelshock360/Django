# modulo do django que cria urls
from django.urls import path
# importe todas suas classes do views.py
from .views import *

urlpatterns = [

    #path (caminho/da/url,ClasseDoView.as_view(),name="nomedessaurl")
	path('',PaginaInicialView.as_view(), name="index"),
    path('sobre/',  SobreView.as_view(), name="sobre"),
	path('curriculo/',  CurriculoView.as_view(), name="curriculo"),
   	path('relatorio/atual/',  VendaRelatirioList.as_view(), name="relatorio"),

	path('formulario/',  FormularioView.as_view(), name="formulario"),
	path('lista/estados/',   EstadoList.as_view(), name="listar-estados"),
	path('lista/cidades/',   CidadeList.as_view(), name="listar-cidades"),
	path('lista/paises/',   PaisList.as_view(), name="listar-paises"),
	path('lista/clientes/',   ClienteList.as_view(), name="listar-clientes"),
	path('lista/funcionarios/',   FuncionarioList.as_view(), name="listar-funcionarios"),
	path('lista/fornecedores/',   FornecedorList.as_view(), name="listar-fornecedores"),
	path('lista/produtos/',   ProdutoList.as_view(), name="listar-produtos"),
	path('lista/vendas/',   VendaList.as_view(), name="listar-vendas"),

   	path('venda/<int:pk>', VendaDetalhes.as_view(),name="detalhes_vendas"),
	# path('funcionario/',  FuncionarioView.as_view(), name="funcionario"),
	# path('cliente/',  ClienteView.as_view(), name="cliente"),

	# path('historico/', HistoricoView.as_view(), name="historico"),

	
    #URLS de cadastros 
    path('cadastrar/estado/',EstadoCreate.as_view(), name="cadastrar-estado"),
	path('editar/estado/<int:pk>/',EstadoUpdate.as_view(), name="editar-estado"),
    path('excluir/estado/<int:pk>/',EstadoDelete.as_view(), name="excluir-estado"),

	  #URLS de cadastros de paises

	path('cadastrar/pais/',PaisCreate.as_view(), name="cadastrar-pais"),
	path('editar/pais/<int:pk>',PaisUpdate.as_view(), name="editar-pais"),
	path('excluir/pais/<int:pk>/',PaisDelete.as_view(), name="excluir-pais"),
	
	 #URLS de cadastros de cidades

	path('cadastrar/cidade/',CidadeCreate.as_view(), name="cadastrar-cidade"),
	path('excluir/cidade/<int:pk>',CidadeDelete.as_view(), name="excluir-cidade"),
	path('editar/cidade/<int:pk>',CidadeUpdate.as_view(), name="editar-cidade"),

	#URLS de cadastros de clientes

	path('cadastrar/cliente/',ClienteCreate.as_view(), name="cadastrar-cliente"),
	path('editar/cliente/<int:pk>',ClienteUpdate.as_view(), name="editar-cliente"),
    path('excluir/cliente/<int:pk>',ClienteDelete.as_view(), name="excluir-cliente"),
	#URLS de cadastros de funcionario

    path('cadastrar/funcionario/',FuncionarioCreate.as_view(), name="cadastrar-funcionario"),
	path('editar/funcionario/<int:pk>',FuncionarioUpdate.as_view(), name="editar-funcionario"),
    path('excluir/funcionario/<int:pk>',FuncionarioDelete.as_view(), name="excluir-funcionario"),

	#URLS de cadastros de fornecedores

	path('cadastrar/fornecedor/',FornecedorCreate.as_view(), name="cadastrar-fornecedor"),
	path('editar/fornecedor/<int:pk>',FornecedorUpdate.as_view(), name="editar-fornecedor"),
	path('excluir/fornecedor/<int:pk>',FornecedorDelete.as_view(), name="excluir-fornecedor"),

	#URLS de cadastros de produto
	path('cadastrar/produto/',ProdutoCreate.as_view(), name="cadastrar-produto"),
	path('editar/produto/<int:pk>',ProdutoUpdate.as_view(), name="editar-produto"),
	path('excluir/produto/<int:pk>',ProdutoDelete.as_view(), name="excluir-produto"),

	#URLS de cadastros de venda
	path('cadastrar/venda/',VendaCreate.as_view(), name="cadastrar-venda"),

]
