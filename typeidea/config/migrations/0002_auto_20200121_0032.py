# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-20 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='herf',
            new_name='href',
        ),
    ]