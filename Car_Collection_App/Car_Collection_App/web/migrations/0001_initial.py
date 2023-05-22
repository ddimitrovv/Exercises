# Generated by Django 4.2.1 on 2023-05-21 21:33

import Car_Collection_App.web.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SPORTS CAR', 'Sports Car'), ('PICKUP', 'Pickup'), ('CROSSOVER', 'Crossover'), ('MINIBUS', 'Minibus'), ('OTHER', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('year', models.IntegerField(validators=[Car_Collection_App.web.models.validate_correct_model_year])),
                ('image', models.URLField(verbose_name='Image URL')),
                ('price', models.FloatField(validators=[Car_Collection_App.web.models.validate_price_is_not_under_one])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[Car_Collection_App.web.models.min_length_validator])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[Car_Collection_App.web.models.min_age_validator])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, default='', max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, default='', max_length=30, verbose_name='Last Name')),
                ('profile_picture', models.URLField(blank=True, default='', verbose_name='Profile Picture')),
            ],
        ),
    ]
