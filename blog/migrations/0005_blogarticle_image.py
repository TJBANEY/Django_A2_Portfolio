# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-29 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_subscriber_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogarticle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
