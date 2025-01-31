# Generated by Django 4.2.18 on 2025-01-30 18:42

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
