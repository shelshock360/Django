# Generated by Django 2.1.7 on 2019-11-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0009_auto_20191112_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='desconto',
            field=models.CharField(blank=True, choices=[(0, 'Venda sem desconto'), ('05%', '05%'), ('10%', '10%'), ('15%', '15%'), ('20%', '20%'), ('25%', '25%')], max_length=4, null=True),
        ),
    ]
