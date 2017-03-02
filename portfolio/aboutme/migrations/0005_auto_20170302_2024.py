# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0004_profile_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='educations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='aboutme.Education'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='aboutme.Job'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='projects.Project'),
        ),
    ]
