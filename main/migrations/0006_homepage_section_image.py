# Generated by Django 5.1.4 on 2025-01-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_ourgallery_homepage_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_image',
            field=models.ImageField(default=1, upload_to='section_image/'),
            preserve_default=False,
        ),
    ]