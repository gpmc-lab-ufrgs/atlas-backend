# Generated by Django 4.0.6 on 2022-10-18 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('state_property', '0001_initial'),
        ('state', '0003_alter_state_geometry'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='properties',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='state_property.stateproperty'),
        ),
    ]