# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0007_auto_20160202_0933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='piece',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='piece',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
