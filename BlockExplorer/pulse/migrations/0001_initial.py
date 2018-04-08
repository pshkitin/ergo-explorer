# Generated by Django 2.0.4 on 2018-04-08 01:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nodeListCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodes', django.contrib.postgres.fields.jsonb.JSONField()),
                ('validTill', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]