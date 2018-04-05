# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0008_compraservicio'),
        ('inventario', '0006_auto_20180405_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='fermentador',
            name='compra',
            field=models.ForeignKey(default=1, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Compra'),
        ),
    ]