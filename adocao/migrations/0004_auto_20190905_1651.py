# Generated by Django 2.1.7 on 2019-09-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0003_venda_valor_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='valor_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]