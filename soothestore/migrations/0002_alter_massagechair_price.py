# Generated by Django 4.2.7 on 2024-01-22 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massagechair',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]