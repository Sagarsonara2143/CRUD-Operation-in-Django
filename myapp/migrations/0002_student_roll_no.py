# Generated by Django 4.2.7 on 2023-11-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
