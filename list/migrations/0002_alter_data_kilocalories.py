# Generated by Django 5.0.2 on 2024-02-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='kilocalories',
            field=models.IntegerField(),
        ),
    ]