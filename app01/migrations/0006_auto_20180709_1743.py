# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-09 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20180709_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(default='avatar/default.png', upload_to='avatar/'),
        ),
    ]
