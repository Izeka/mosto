# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0047_auto_20171106_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coccion',
            name='Tiempo_Hervor',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Tiempo_Hervor',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
    ]