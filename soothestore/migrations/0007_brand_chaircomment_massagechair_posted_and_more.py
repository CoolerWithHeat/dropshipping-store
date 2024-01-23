# Generated by Django 4.2.7 on 2024-01-23 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0006_remove_massagechair_product_rating_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=20)),
                ('authorized_in', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChairComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.CharField(default='Anonymous', max_length=35)),
                ('comment_text', models.TextField(default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='massagechair',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='massagechair',
            name='brand',
            field=models.CharField(choices=[('kahuna', 'Kahuna'), ('osaki', 'Osaki'), ('real_relax', 'real Relax')], default=('kahuna', 'Kahuna'), max_length=35),
        ),
    ]
