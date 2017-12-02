# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20171202_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='tags',
            field=models.ManyToManyField(to='events.Tag'),
        ),
    ]
