# Generated by Django 4.2.7 on 2024-01-27 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0002_brand_chairfeature_chairtype_color_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massagechair',
            name='brand',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='soothestore.brand'),
        ),
    ]