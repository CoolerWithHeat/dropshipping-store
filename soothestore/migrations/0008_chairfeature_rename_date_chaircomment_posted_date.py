# Generated by Django 4.2.7 on 2024-01-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0007_brand_chaircomment_massagechair_posted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChairFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('called', models.CharField(max_length=60)),
            ],
        ),
        migrations.RenameField(
            model_name='chaircomment',
            old_name='date',
            new_name='posted_date',
        ),
    ]