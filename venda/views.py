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
    model = ItensCarrinho
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
    template_name = "venda/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("lista-vender-produtos")
    # quais campos vai aparecer no formulario
    fields = ['produto', 'quantidade', 'informacoes_adicionais']

    def get_context_data(self, *args, **kwargs):
        context = super( ProdutoCreateCarrinhoVenda, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Adicionar produto na venda"
        context['botao'] = "Adicionar"
        context['classbotao'] = "btn-success"
        context['urlvoltar'] = "lista-vender-produtos"

        return context


class ProdutoUpdateCarrinhoVenda (LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe

    model = ItensCarrinho
    template_name = "venda/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("lista-vender-produtos")
    # quais campos vai aparecer no formulario
    fields = ['produto', 'quantidade', 'informacoes_adicionais']

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoUpdateCarrinhoVenda, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Atualizar produto da venda"
        context['botao'] = "Atualizar"
        context['classbotao'] = "btn-success"
        context['urlvoltar'] = "lista-vender-produtos"

        return context


class ProdutoDeleteCarrinhoVenda (LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe

    model = ItensCarrinho
    template_name = "venda/formulario.html"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("lista-vender-produtos")
    # quais campos vai aparecer no formulario

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoDeleteCarrinhoVenda, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Remover produto da venda"
        context['botao'] = "Remover"
        context['classbotao'] = "btn-danger"
        context['urlvoltar'] = "lista-vender-produtos"

        return context







