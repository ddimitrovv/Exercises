from django.core import validators
from django.db import models
from django.core.exceptions import ValidationError


MIN_AGE_VALUE = 18


def min_length_validator(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def min_age_validator(value):
    if value < MIN_AGE_VALUE:
        raise ValidationError('Age cannot be below 18')


def validate_correct_model_year(value):
    if not 1980 <= value <= 2049:
        raise ValidationError('Year must be between 1980 and 2049')


def validate_price_is_not_under_one(value):
    if value < 1:
        raise ValidationError('Price cannot be below 1')


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    PASSWORD_MAX_LENGTH = 30
    NAME_MAX_LENGTH = 30

    username = models.CharField(
        null=False,
        blank=False,
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            min_length_validator,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            min_age_validator,
        ),
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=PASSWORD_MAX_LENGTH,
    )

    first_name = models.CharField(
        blank=True,
        default='',
        max_length=NAME_MAX_LENGTH,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        blank=True,
        default='',
        max_length=NAME_MAX_LENGTH,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        blank=True,
        default='',
        verbose_name='Profile Picture',
    )


class Car(models.Model):
    CHARACTER_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 2

    CHOICES = (
        ('SPORTS CAR', 'Sports Car',),
        ('PICKUP', 'Pickup'),
        ('CROSSOVER', 'Crossover'),
        ('MINIBUS', 'Minibus'),
        ('OTHER', 'Other'),
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=CHARACTER_MAX_LENGTH,
        choices=CHOICES,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MODEL_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(MODEL_MIN_LENGTH),
        ),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validate_correct_model_year,
        ),
    )

    image = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validate_price_is_not_under_one,
        ),
    )
