# Generated by Django 4.0.6 on 2022-10-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='type',
            field=models.CharField(choices=[('S', 'state'), ('D', 'district')], default='S', max_length=1),
        ),
    ]
