# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0018_auto_20171101_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
