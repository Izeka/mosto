# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20180323_1204'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Forma',
        ),
        migrations.AlterField(
            model_name='insumo',
            name='Tipo',
            field=models.CharField(choices=[('INSUMO', 'Insumo'), ('INGREDIENTE', 'Ingrediente'), ('EQUIPAMIENTO', 'Equipamiento')], error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=10),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='Unidad_de_medida',
            field=models.CharField(blank=True, choices=[('Kg', 'Kilogramos'), ('g', 'Gramos'), ('l', 'Litros')], error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
        migrations.DeleteModel(
            name='Unidad_medida',
        ),
    ]
