# Generated by Django 5.1.4 on 2024-12-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
