from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


class Profile(models.Model):
    USER_NAME_MAX_LEN = 10
    USER_NAME_MIN_LEN = 2

    AGE_MIN_VALUE = 18

    PASSWORD_MAX_LEN = 30

    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    user_name = models.CharField(
        max_length=USER_NAME_MAX_LEN,
        verbose_name="Username",
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(USER_NAME_MIN_LEN,
                                          message="The username must be a minimum of 2 chars"),
        )
    )
    email = models.EmailField(
        null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(AGE_MIN_VALUE),
        )
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        null=False,
        blank=False
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        verbose_name='First Name',
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        verbose_name='Last Name',
        null=True,
        blank=True
    )
    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True
    )


def year_range_validator_1980_2049(value):
    if value < 1980 or value > 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class Car(models.Model):
    TYPE_MAX_LEN = 10

    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2

    PRICE_MIN_VALUE = 1

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER)
    )
    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=TYPES,
        null=False,
        blank=False
    )
    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MODEL_MIN_LEN),
        )
    )
    year = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            year_range_validator_1980_2049,
        )
    )
    image_url = models.URLField(
        verbose_name="Image URL",
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(PRICE_MIN_VALUE),
        )
    )
