# Generated by Django 5.0.6 on 2024-05-14 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_constructeur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constructeur',
            old_name='nom',
            new_name='marque',
        ),
        migrations.AddField(
            model_name='mobile',
            name='constructeur',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.constructeur'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='prix',
            field=models.FloatField(),
        ),
    ]
