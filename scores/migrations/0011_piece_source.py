# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-06 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0010_auto_20170506_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transcribed', to='scores.Editor'),
        ),
    ]
