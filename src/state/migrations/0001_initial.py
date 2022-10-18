# Generated by Django 4.0.6 on 2022-10-18 20:37

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('name', models.CharField(default='state', max_length=255, primary_key=True, serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(blank=True, default=django.contrib.gis.geos.point.Point(0, 0), srid=4326)),
            ],
        ),
    ]
