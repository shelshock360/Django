from django.shortcuts import render
# importar todas as classes de models.py
from .models import *
from venda.models import ItensCarrinho
from django.views.generic import TemplateView

from django.urls import reverse_lazy

# importaçao pra alterar excluir consultar
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

from django.contrib.auth.models import User, Group

from django.shortcuts import get_object_or_404
# Create your views here.


from django.views.generic.detail import DetailView
class PaginaInicialView(TemplateView):
    # nome do arquivo que sera ultilizado para renderizar
    template_name = "adocao/index.html"
    # estapagina/metodo/classe


class SobreView(TemplateView):
    template_name = "adocao/sobre.html"


class CurriculoView(TemplateView):
    template_name = "adocao/curriculo.html"


# class RelatorioView(TemplateView):
#     template_name = "adocao/relatorio.html"


class FormularioView(TemplateView):
    template_name = "adocao/formulario.html"




##############################INSERIR ###################


class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    # defini qual o modelo pra classe

    model = Estado
    template_name = "adocao/formulario.html"
    group_required = u"gerente"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-estados")
    # quais campos vai aparecer no formulario
    fields = ['sigla', 'nome', 'pais']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(EstadoCreate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context
##############################Alterar ###################


class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe

    model = Estado
    template_name = "adocao/formulario.html"
    group_required = u"gerente"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-estados")
    # quais campos vai aparecer no formulario
    fields = ['sigla', 'nome', 'pais']

    def get_context_data(self, *args, **kwargs):
        context = super(EstadoUpdate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "editar novos Estados"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"
        return context


class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe

    model = Estado
    template_name = "adocao/formulario.html"
    group_required = u"gerente"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-estados")
    # quais campos vai aparecer no formulario

    def get_context_data(self, *args, **kwargs):
        context = super(EstadoDelete, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "excluir registro de estados"
        context['botao'] = "Excluir"
        context['classbotao'] = "btn-danger"

        return context


class EstadoList(GroupRequiredMixin,LoginRequiredMixin, ListView):
    model = Estado
    template_name = "adocao/listar_estados.html"
    group_required = u"gerente"

    ######################Paises##############

class PaisCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    # defini qual o modelo pra classe

    model = Pais
    template_name = "adocao/formulario.html"
    group_required = u"gerente"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-paises")
    # quais campos vai aparecer no formulario
    fields = ['nome']

    def get_context_data(self, *args, **kwargs):
        context = super(PaisCreate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastro de novos Paises"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class PaisList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"gerente"
    model = Pais
    template_name = "adocao/listar_paises.html"


class PaisDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe

    model = Pais
    template_name = "adocao/formulario.html"
    group_required = u"gerente"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-paises")
    # quais campos vai aparecer no formulario

    def get_context_data(self, *args, **kwargs):
        context = super(PaisDelete, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "excluir registro de paises "
        context['botao'] = "Excluir"
        context['classbotao'] = "btn-danger"

        return context


class PaisUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe

    model = Pais
    template_name = "adocao/formulario.html"
    group_required = u"gerente"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-paises")
    # quais campos vai aparecer no formulario
    fields = ['nome']

    def get_context_data(self, *args, **kwargs):
        context = super(PaisUpdate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "editar novos paises"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context

     ######################Cidades##############


class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    # defini qual o modelo pra classe

    model = Cidade
    template_name = "adocao/formulario.html"
    group_required = u"gerente"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-cidades")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'estado', 'descricao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeCreate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastro de novas Cidades"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe

    model = Cidade
    template_name = "adocao/formulario.html"
    group_required = u"gerente"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-cidades")
    # quais campos vai aparecer no formulario

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeDelete, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "excluir registro de cidades"
        context['botao'] = "Excluir"
        context['classbotao'] = "btn-danger"

        return context


class CidadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Cidade
    template_name = "adocao/listar_cidades.html"
    group_required = u"gerente"

class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe

    model = Cidade
    template_name = "adocao/formulario.html"
    group_required = u"gerente"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-cidades")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'estado', 'descricao']

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeUpdate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "editar novas cidades"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


##############################Clientes###########


class ClienteCreate(LoginRequiredMixin, CreateView):
    # defini qual o modelo pra classe
    model = Cliente
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-clientes")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'rg', 'cpf', 'endereco',
              'cidade', 'telefone', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(ClienteCreate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastro de novos Clientes"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "adocao/listar_clientes.html"


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe

    model = Cliente
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-clientes")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'rg', 'cpf', 'endereco',
              'cidade', 'telefone', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(ClienteUpdate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "editar cliente"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class ClienteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe

    model = Cliente
    template_name = "adocao/formulario.html"
    group_required = u"gerente"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-clientes")
    # quais campos vai aparecer no formulario

    def get_context_data(self, *args, **kwargs):
        context = super(ClienteDelete, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "excluir registro de cliente"
        context['botao'] = "Excluir"
        context['classbotao'] = "btn-danger"

        return context

   #################### Funcionario ###########


class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    # defini qual o modelo pra classe
    group_required = u"gerente"
    model = Funcionario
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-funcionarios")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'cpf', 'cargo', 'cidade',
              'data_contratacao', 'salario', 'email', 'usuario', 'senha', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(FuncionarioCreate, self).get_context_data(
            *args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastro de novos funcionarios"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"
        return context

    def form_valid(self, form):

        # Recebe os dados do formulário
        senha = form.cleaned_data['senha']
        email = form.cleaned_data['email']
        usuario = form.cleaned_data['usuario']
        cargo = form.cleaned_data['cargo']

        # Tenta criar um usuário
        try:
            user = User.objects.create_user(usuario, email, senha)
            # Adicionar o usuário no grupo
            if (cargo == "VENDEDOR"):
                grupo = Group.objects.get(name='VENDEDOR')
                user.groups.add(grupo)
                user.save()
            # Ou fazer ele um admin/superuser
            elif (cargo == "GERENTE"):
                grupo = Group.objects.get(name='GERENTE')
                user.groups.add(grupo)
                user.is_superuser = True
                user.save()
        except:
            # try
            user.delete()
            # except:
            #     pass
            form.add_error(
                None, 'Erro ao tentar cadastrar esse funcionário como usuário.')
            return self.form_invalid(form)

        # "ligar" o usuário criado com o funcionário que vai ser cadastrado
        form.instance.user = user
        # Se tudo ocorreu bem, finaliza
        return super(FuncionarioCreate, self).form_valid(form)


class FuncionarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"gerente"
    model = Funcionario
    template_name = "adocao/listar_funcionarios.html"


class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe

    model = Funcionario
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-funcionarios")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'cpf', 'cidade', 'cargo',
              'data_contratacao', 'salario', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(FuncionarioUpdate, self).get_context_data(
            *args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "editar funcionarios"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class FuncionarioDelete(LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe

    model = Funcionario
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-funcionarios")
    # quais campos vai aparecer no formulario

    def get_context_data(self, *args, **kwargs):
        context = super(FuncionarioDelete, self).get_context_data(
            *args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "excluir registro de funcionario"
        context['botao'] = "Excluir"
        context['classbotao'] = "btn-danger"

        return context

    ###################### Fornecedores ###################


class FornecedorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    # defini qual o modelo pra classe
    group_required = u"gerente"
    model = Fornecedor
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-fornecedores")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'cnpj', 'endereco', 'pais',
              'cidade', 'telefone', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(FornecedorCreate, self).get_context_data(
            *args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastrar novo Fornecedor"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class FornecedorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"gerente"
    model = Fornecedor
    template_name = "adocao/listar_fornecedores.html"


class FornecedorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe
    group_required = u"gerente"
    model = Fornecedor
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-fornecedores")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'cnpj', 'endereco', 'pais',
              'cidade', 'telefone', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(FornecedorUpdate, self).get_context_data(
            *args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastro de novos Fornecedores"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class FornecedorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe
    group_required = u"gerente"
    model = Fornecedor
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-fornecedores")
    # quais campos vai aparecer no formulario

    def get_context_data(self, *args, **kwargs):
        context = super(FornecedorDelete, self).get_context_data(
            *args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "excluir registro de fornecedor"
        context['botao'] = "Excluir"
        context['classbotao'] = "btn-danger"

        return context


################## Produto ####################
class ProdutoCreate(LoginRequiredMixin, CreateView):
    # defini qual o modelo pra classe

    model = Produto
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-produtos")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'marca', 'fornecedor', 'modelo',
              'valor_venda', 'data_chegada', 'qtde_estoque', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoCreate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastro de novos Produtos"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class ProdutoList(LoginRequiredMixin, ListView):
    model = Produto
    template_name = "adocao/listar_produtos.html"


class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe

    model = Produto
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-produtos")
    # quais campos vai aparecer no formulario
    fields = ['nome', 'marca', 'modelo', 'fornecedor',
              'valor_venda', 'data_chegada', 'qtde_estoque', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoUpdate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "editar produto "
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"
        return context


class ProdutoDelete(LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe

    model = Produto
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-produtos")
    # quais campos vai aparecer no formulario

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoDelete, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "excluir registro de produto"
        context['botao'] = "Excluir"
        context['classbotao'] = "btn-danger"

        return context


class VendaCreate(LoginRequiredMixin, CreateView):
    # defini qual o modelo pra classe

    model = Venda
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("listar-vendas")
    # quais campos vai aparecer no formulario
    fields = ['cliente', 'data_venda', 'desconto', 'observacao']
    # metodo ultilizado para enviar dados ao template

    """ Método que é chamadao para validar o formulário e salvar o objeto no banco """

    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        # Executa o form_valid padrão para validar e salvar no banco de dados
        redirect_url = super(VendaCreate, self).form_valid(form)

        # Cria uma variável pra essa venda
        valorTotal = 0

        """ Agora temos a venda no banco, vamos pegar os produtos do carrinho e salvar nessa venda """
        # buscar todos os objetos da classe ItensCarrinho no banco
        produtosCarrinho = ItensCarrinho.objects.all()

        # Para cada produto no carrinho, salva no ItemsVenda (foreach)
        for itemCarrinho in produtosCarrinho:

            # Calcula o subtotal = quantidade x valor do produto
            subtotal = itemCarrinho.produto.valor_venda * itemCarrinho.quantidade
            # Atualiza o valor total da venda
            valorTotal = valorTotal + subtotal

            # Cria um objeto no ItemsVenda no banco de dados para saber os produtos que foram vendidos
            ItemsVenda.objects.create(
                preco=subtotal,
                qtde=itemCarrinho.quantidade,
                produto=itemCarrinho.produto,
                venda=self.object
            )

            # Da baixa no estoque no produto
            itemCarrinho.produto.qtde_estoque = itemCarrinho.produto.qtde_estoque - \
                itemCarrinho.quantidade
            # Atualiza o produto no banco de dados
            itemCarrinho.produto.save()

            # Deleta o item do carrinho
            itemCarrinho.delete()

        # Atualiza o objeto dessa venda com o valor total
        # Primeiro tira a % do desconto e transforma ele para inteiro e depois faz a conta
        desconto = valorTotal * int(self.object.desconto.replace("%", "")) / 100
        # Define o valor bruto (sem desconto)
        self.object.valor_bruto = valorTotal
        # Calcula o valor com desconto
        self.object.valor_total = self.object.valor_bruto - desconto
        # Salva a venda
        self.object.save()

        # Fim do form_valid
        return redirect_url

    def get_context_data(self, *args, **kwargs):
        context = super(VendaCreate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "vender produto"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class VendaList(LoginRequiredMixin, ListView):
    model = Venda
    template_name = "adocao/listar_vendas.html"


class VendaRelatirioList(LoginRequiredMixin, ListView):
    model = Venda
    template_name = "adocao/relatorio.html"


class VendaUpdate(LoginRequiredMixin, UpdateView):
    # defini qual o modelo pra classe

    model = Venda
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("index")
    # quais campos vai aparecer no formulario
    fields = ['cliente', 'data_venda', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(VendaUpdate, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "editar venda produto"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context


class VendaDelete(LoginRequiredMixin, DeleteView):
    # defini qual o modelo pra classe

    model = Venda
    template_name = "adocao/formulario.html"

    # Pra onde redirecionar o usuario  depois de inserir
    success_url = reverse_lazy("index")
    # quais campos vai aparecer no formulario
    fields = ['cliente', 'data_venda', 'vendedor', 'observacao']
# metodo ultilizado para enviar dados ao template

    def get_context_data(self, *args, **kwargs):
        context = super(VendaDelete, self).get_context_data(*args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "excluir registro de venda"
        context['botao'] = "Excluir"
        context['classbotao'] = "btn-danger"

        return context

################## Detalhar ##################


class VendaDetalhes(LoginRequiredMixin,DetailView):

    model = Venda
    template_name = "adocao/detalhes_vendas.html"


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 

        context['produtos'] = ItemsVenda.objects.filter(venda=self.object)

        return context


class EntradaProdutoCreate (LoginRequiredMixin, CreateView):

    model = EntradaProduto
    template_name= "adocao/formulario.html"
    fields = ['qtde', 'data_chegada','produto', 'observacao']
    success_url = reverse_lazy("listar-produtos")
    
       
    def get_context_data(self, *args, **kwargs):
        context = super(EntradaProdutoCreate, self).get_context_data(
            *args, **kwargs)

        # adiciona coisas ao contextos das coisas
        context['titulo'] = "Cadastrar produto recem chegado a loja"
        context['botao'] = "Cadastrar"
        context['classbotao'] = "btn-success"

        return context
    
    
    def form_valid(self, form):
        redirect_url = super(EntradaProdutoCreate, self).form_valid(form)
        print("quantidade",self.object.produto.qtde_estoque) 
        self.object.produto.qtde_estoque += self.object.qtde
        print("quantidade",self.object.produto.qtde_estoque) 
        self.object.produto.data_chegada = self.object.data_chegada
        self.object.produto.save()
        
        return redirect_url
