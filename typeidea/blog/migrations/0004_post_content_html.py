# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-30 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200124_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_html',
            field=models.TextField(blank=True, editable=False, verbose_name='正文HTML代码'),
        ),
    ]
