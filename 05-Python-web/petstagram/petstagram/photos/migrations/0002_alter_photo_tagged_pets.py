# Generated by Django 4.1.2 on 2022-10-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pet_slug'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, to='pets.pet'),
        ),
    ]
