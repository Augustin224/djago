# Generated by Django 5.1.1 on 2024-09-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.FloatField(null=True),
        ),
    ]
