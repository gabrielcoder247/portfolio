# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-15 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfolio', '0002_auto_20180711_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=2, upload_to='uploads'),
            preserve_default=False,
        ),
    ]
