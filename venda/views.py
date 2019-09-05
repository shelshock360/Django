from django.shortcuts import render

from .models import ItensCarrinho
from adocao.models import Produto

from django.views.generic import TemplateView

from django.urls import reverse_lazy

# importaçao pra alterar excluir consultar
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# Criar um CreateView para ItensCarrinho - Link Adicionar Produto (base.html)

# Criar um UpdateView para ItensCarrinho

# Criar um DeleteView para ItensCarrinho

# Criar um ListView para ItensCarrinho - Link Carrinho de Vendas (base.html)

class ProdutoListCarrinhoVenda(LoginRequiredMixin, ListView):
    model = Produto
    template_name = "venda/listar_produtos.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoListCarrinhoVenda,
                        self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['teste'] = "bla bla"

        return context


class ProdutoCreateCarrinhoVenda (LoginRequiredMixin, CreateView):
    # defini qual o modelo pra classe

    model = ItensCarrinho
    template_name = "venda/listar_produtos.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("lista-vender-produtos")
    # quais campos vai aparecer no formulario
    fields = ['produto', 'quantidade']

    def get_context_data(self, *args, **kwargs):
        context = super( ProdutoCreateCarrinhoVenda, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "vendas"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class ProdutoUpdateCarrinhoVenda (LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe

    model = ItensCarrinho
    template_name = "venda/listar_produtos.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("lista-vender-produtos")
    # quais campos vai aparecer no formulario
    fields = ['produto', 'quantidade']

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoUpdateCarrinhoVenda, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "editar vendas"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"
        return context


class ProdutoDeleteCarrinhoVenda (LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe

    model = ItensCarrinho
    template_name = "venda/listar_produtos.html"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-estados")
    # quais campos vai aparecer no formulario

    def get_context_data(self, *args, **kwargs):
        context = super(EstadoDelete, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "excluir registro de venda"
        context['botao'] = "Excluir"
        context['classbotao'] = "btn-danger"

        return context







