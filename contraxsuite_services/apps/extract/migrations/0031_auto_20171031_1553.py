# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract', '0030_auto_20171031_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='type_abbr',
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='type_description',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='type_label',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
    ]
