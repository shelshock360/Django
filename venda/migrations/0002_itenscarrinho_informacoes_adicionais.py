# Generated by Django 2.1.7 on 2019-09-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itenscarrinho',
            name='informacoes_adicionais',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Informações adicionais'),
        ),
    ]