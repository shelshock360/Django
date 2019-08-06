# Generated by Django 2.1.7 on 2019-08-06 18:28

import adocao.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, help_text='espaço para colocar qualquer informação', null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('rg', models.CharField(max_length=20, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[adocao.models.validate_CPF])),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('observacao', models.TextField(blank=True, help_text='qual quer informação extra sobre o cliente', null=True, verbose_name='Observação')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2, unique=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=18, unique=True, validators=[adocao.models.validate_CNPJ])),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('observacao', models.TextField(blank=True, help_text='qual quer informação extra sobre o fornecedor', null=True, verbose_name='Observação')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[adocao.models.validate_CPF])),
                ('cargo', models.CharField(choices=[('GERENTE', 'GERENTE'), ('VENDEDOR', 'VENDEDOR')], max_length=10)),
                ('data_contratacao', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('senha', models.CharField(max_length=20)),
                ('observacao', models.TextField(blank=True, help_text='qual quer informação extra sobre o funcionario', null=True, verbose_name='Observação')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Cidade')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('qtde', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(blank=True, max_length=50)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_chegada', models.DateField()),
                ('qtde_estoque', models.IntegerField()),
                ('observacao', models.TextField(blank=True, help_text='qual quer informação extra sobre produto', null=True, verbose_name='Observação')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateField()),
                ('observacao', models.TextField(blank=True, help_text='qual quer informação adicional para a venda', null=True, verbose_name='Observação')),
                ('qtde', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Produto')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Funcionario')),
            ],
        ),
        migrations.AddField(
            model_name='itemsvenda',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Produto'),
        ),
        migrations.AddField(
            model_name='itemsvenda',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Venda'),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Pais'),
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Pais'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adocao.Estado'),
        ),
    ]
