# Generated by Django 2.1.7 on 2019-10-05 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0004_auto_20190905_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
