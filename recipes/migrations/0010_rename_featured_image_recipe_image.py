# Generated by Django 4.2.18 on 2025-02-01 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_recipe_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='featured_image',
            new_name='image',
        ),
    ]
