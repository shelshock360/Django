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
