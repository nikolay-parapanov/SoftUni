# Generated by Django 4.1.3 on 2022-11-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
