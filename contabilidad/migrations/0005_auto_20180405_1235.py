# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0004_auto_20180404_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprabarril',
            name='barril',
            field=models.ForeignKey(error_messages={b'invalid': b'Ingrese un valor valido', b'required': b'Este valor es requerido', b'unique': b'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, related_name='add_barril', to='inventario.Barril'),
        ),
    ]
