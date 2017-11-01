# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0013_auto_20171027_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='Temp_Coccion',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='Tiempo_Coccion',
        ),
        migrations.AlterField(
            model_name='agregados_x_receta',
            name='Agregados',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='inventario.Agregado'),
        ),
        migrations.AlterField(
            model_name='agregados_x_receta',
            name='Cantidad',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='agregados_x_receta',
            name='Receta',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Receta'),
        ),
        migrations.AlterField(
            model_name='estilo',
            name='Nombre',
            field=models.CharField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='levadura_x_receta',
            name='Cantidad',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='levadura_x_receta',
            name='Levadura',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='inventario.Levadura'),
        ),
        migrations.AlterField(
            model_name='levadura_x_receta',
            name='Receta',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Receta'),
        ),
        migrations.AlterField(
            model_name='lupulo_x_receta',
            name='Cantidad',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='lupulo_x_receta',
            name='Lupulo',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='inventario.Lupulo'),
        ),
        migrations.AlterField(
            model_name='lupulo_x_receta',
            name='Receta',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Receta'),
        ),
        migrations.AlterField(
            model_name='lupulo_x_receta',
            name='Tiempo',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AlterField(
            model_name='malta_x_receta',
            name='Cantidad',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='malta_x_receta',
            name='Malta',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='inventario.Malta'),
        ),
        migrations.AlterField(
            model_name='malta_x_receta',
            name='Receta',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Receta'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Alcohol',
            field=models.FloatField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='DF',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AlterField(
            model_name='receta',
            name='DI',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AlterField(
            model_name='receta',
            name='EBC',
            field=models.IntegerField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Eficiencia',
            field=models.IntegerField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='IBUs',
            field=models.FloatField(blank=True, error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Litros',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Nombre',
            field=models.CharField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Temp_Fermantacion',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Temp_Maceracion',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Tiempo_Fermentacion',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Tiempo_Maceracion',
            field=models.IntegerField(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Tipo',
            field=models.ForeignKey(error_messages={'invalid': 'Ingrese un valor valido', 'required': 'Este valor es requerido', 'unique': 'Este valor ya fue utilizado'}, on_delete=django.db.models.deletion.CASCADE, to='produccion.Estilo'),
        ),
    ]
