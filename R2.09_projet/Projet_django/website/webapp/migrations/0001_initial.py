# Generated by Django 5.0.6 on 2024-05-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date_parution', models.DateField(blank=True, null=True)),
                ('prix', models.IntegerField()),
            ],
        ),
    ]