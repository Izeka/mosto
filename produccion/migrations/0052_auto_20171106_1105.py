# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0051_auto_20171106_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coccion',
            name='Observaciones',
            field=models.TextField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100),
        ),
    ]