# Generated by Django 4.2.18 on 2025-01-30 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_recipe_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edit', to='recipes.recipe'),
        ),
    ]
