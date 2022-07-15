# Generated by Django 4.0.4 on 2022-05-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0003_alter_requestrecipe_rrec_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestrecipe',
            name='rrec_type',
            field=models.CharField(choices=[('VEG', 'Vegetarian'), ('NVEG', 'Non Vegetarian'), ('VEGAN', 'Vegan')], max_length=5),
        ),
    ]
