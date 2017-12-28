# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0019_auto_20171101_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='agregados_x_receta',
            name='Tiempo',
            field=models.IntegerField(default=None, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
    ]