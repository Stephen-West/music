# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0008_auto_20160202_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='lulu',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
