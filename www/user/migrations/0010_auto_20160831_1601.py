# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20160831_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myrecommend',
            old_name='audio_for_qian',
            new_name='audio_for_qlm',
        ),
        migrations.RenameField(
            model_name='myrecommend',
            old_name='audio_for_zhu',
            new_name='audio_for_zg',
        ),
    ]
