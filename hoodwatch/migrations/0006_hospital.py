# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-16 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodwatch', '0005_auto_20190916_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
