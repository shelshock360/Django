from django.db import models
from django.forms import ValidationError
from adocao.models import Produto
from django.contrib.auth.models import User


class ItensCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.produto.nome + ' x ' + self.quantidade
