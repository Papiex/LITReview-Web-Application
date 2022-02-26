# Generated by Django 4.0.1 on 2022-02-25 13:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=8192),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[('&#9734;&#9734;&#9734;&#9734;&#9734;', '0'), ('&#9733;&#9734;&#9734;&#9734;&#9734;', '1'), ('&#9733;&#9733;&#9734;&#9734;&#9734;', '2'), ('&#9733;&#9733;&#9733;&#9734;&#9734;', '3'), ('&#9733;&#9733;&#9733;&#9733;&#9734;', '4'), ('&#9733;&#9733;&#9733;&#9733;&#9733;', '5')], validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
