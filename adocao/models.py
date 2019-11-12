import re
from django.db import models
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


error_messages = {
    'invalid': _("Invalid CPF number."),
    'digits_only': _("This field requires only numbers."),
    'max_digits': _("This field requires exactly 11 digits."),
}


def DV_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_CPF(value):
    """
    Value can be either a string in the format XXX.XXX.XXX-XX or an
    11-digit number.
    """

    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError(error_messages['digits_only'])
    if len(value) != 11:
        raise ValidationError(error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx])
                   for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx])
                   for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid'])

    return orig_value
#_________________________________________________#


def validate_CNPJ(value):
    """
    Value can be either a string in the format XX.XXX.XXX/XXXX-XX or a
    group of 14 characters.
    :type value: object
    """
    value = str(value)
    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-/\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError(error_messages['digits_only'])
    if len(value) > 14:
        raise ValidationError(error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx,
                   i in enumerate(list(range(5, 1, -1)) + list(range(9, 1, -1)))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx,
                   i in enumerate(list(range(6, 1, -1)) + list(range(9, 1, -1)))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid'])

    return orig_value
#____________________________#
# Create your models here.


class Pais (models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Estado (models.Model):
    # nome_doatributo= models.Tipo(configuraçao)
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    # como se fosse o toString e sefl = this

    def __str__(self):
        return self.sigla + '-' + self.nome


class Cidade (models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição",
                                 help_text="espaço para colocar qualquer informação")

    def __str__(self):
        return self.nome + "-" + self.estado.sigla


class Cliente (models.Model):
    nome = models.CharField(max_length=50, unique=True)
    rg = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=14, unique=True,validators=[validate_CPF])
    endereco = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    telefone = models.CharField(max_length=20)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação",help_text="qual quer informação extra sobre o cliente")

    def __str__(self):
        return self.nome 




class Funcionario (models.Model):

    CARGO_CHOICES = (
        (u'GERENTE', u'GERENTE'),
        (u'VENDEDOR', u'VENDEDOR'),
    )

    nome = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=14, unique=True,
                           validators=[validate_CPF])
                              
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    cargo = models.CharField(max_length=10, choices=CARGO_CHOICES)
    data_contratacao = models.DateField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    email = models.EmailField(unique=True)
    usuario=models.CharField(max_length=20,unique=True)
    senha = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação",
                                  help_text="qual quer informação extra sobre o funcionario")

    def __str__(self):

        return self.nome + "-" + str(self.data_contratacao)




class Fornecedor (models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18, unique=True, validators=[validate_CNPJ])
    endereco = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    telefone= models.CharField(max_length=20)
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação", help_text="qual quer informação extra sobre o fornecedor")

    def __str__(self):
        return self.nome + "-"+self.cnpj+"-" + self.endereco + "-"+self.telefone


class Produto (models.Model):
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=50, blank=True)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_chegada = models.DateField()
    qtde_estoque = models.IntegerField()
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação", help_text="qual quer informação extra sobre produto")

    def __str__(self):
        return self.nome + "-"+str(self.valor_venda)+"-" + str(self.data_chegada)





class Venda (models.Model):

    DESCONTO_CHOICES = (
        (u"00%", u'Venda sem desconto'),
        (u'05%', u'05%'),
        (u'10%', u'10%'),
        (u'15%', u'15%'),
        (u'20%', u'20%'),
        (u'25%', u'25%'),
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_venda = models.DateField()
    vendedor = models.ForeignKey(User, on_delete=models.PROTECT)    
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação",  help_text="qual quer informação adicional para a venda")
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    valor_bruto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    desconto = models.CharField(max_length=4, null=True, blank=True, choices=DESCONTO_CHOICES)
    # produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    # qtde = models.IntegerField()
    

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.data_venda) + ' | ' + self.cliente.nome + ' | ' + str(self.valor_total)
        
class ItemsVenda(models.Model):
      preco = models.DecimalField(max_digits=8, decimal_places=2)
      qtde = models.IntegerField()
      produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
      venda = models.ForeignKey(Venda, on_delete=models.PROTECT)
      def __str__(self):
        return "[Venda ID: " + str(self.venda.pk) + "] " + self.produto.nome + " x " + str(self.qtde) + " = " + str(self.preco)
