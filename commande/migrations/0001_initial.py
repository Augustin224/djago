# Generated by Django 5.1.1 on 2024-09-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(choices=[('en_instance', 'en_instance'), ('non livré', 'non livré'), ('livré', 'livré')], max_length=200, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
