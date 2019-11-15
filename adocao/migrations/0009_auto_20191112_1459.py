# Generated by Django 2.1.7 on 2019-11-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0008_venda_desconto'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='valor_bruto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='venda',
            name='desconto',
            field=models.DecimalField(blank=True, choices=[(0, 'Venda sem desconto'), (0.05, '05%'), (0.1, '10%'), (0.15, '15%'), (0.2, '20%'), (0.25, '25%')], decimal_places=2, max_digits=8, null=True),
        ),
    ]