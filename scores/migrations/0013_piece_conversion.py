# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0012_licensing_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='conversion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='converted', to='scores.Editor'),
        ),
    ]