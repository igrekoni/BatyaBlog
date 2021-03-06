# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 11:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170908_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=posts.models.upload_location, width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
