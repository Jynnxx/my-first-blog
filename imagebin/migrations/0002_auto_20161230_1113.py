# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-30 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagebin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
