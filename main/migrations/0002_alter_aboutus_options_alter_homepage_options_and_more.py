# Generated by Django 5.1.4 on 2024-12-19 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'About Us Banner', 'verbose_name_plural': 'About Us Banner'},
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'Home Page'},
        ),
        migrations.AlterModelOptions(
            name='parquet',
            options={'verbose_name': 'Parquet Banners', 'verbose_name_plural': 'Parquet Banners'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Projects Banner', 'verbose_name_plural': 'Projects Banner'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Reviews Banner', 'verbose_name_plural': 'Reviews Banner'},
        ),
        migrations.AddField(
            model_name='aboutuscard',
            name='about_us',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.aboutus'),
            preserve_default=False,
        ),
    ]
