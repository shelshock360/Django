# Generated by Django 2.1.7 on 2019-09-05 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='qtde',
        ),
    ]
