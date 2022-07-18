# Generated by Django 4.0.4 on 2022-05-13 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0006_remove_recipe_info_meal_alter_catdetails_cat_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='ing_type',
            field=models.CharField(choices=[('Recipe Base', 'Recipe Base'), ('Vegetables & Greens', 'Vegetables & Greens'), ('Fruits & Berries', 'Fruits & Berries'), ('Baking', 'Baking'), ('Dairy & Eggs', 'Dairy & Eggs'), ('Herbs & Spices', 'Herbs & Spices')], default='Vegetable & Green', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe_info',
            name='rec_type',
            field=models.CharField(choices=[('veg', 'Veg'), ('non-veg', 'Non-Veg'), ('vegan', 'Vegan')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='requestrecipe',
            name='cat_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='instaapp.catdetails'),
        ),
    ]