from django.core import validators, exceptions
from django.core.exceptions import ValidationError
from django.db import models


def validator_only_alphanumeric_and_underscore(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError('Ensure this value contains only letters, numbers, and underscore.')

class Profile(models.Model):
    USER_NAME_MAX_LEN = 15
    USER_NAME_MIN_LEN = 2

    AGE_MIN_AGE =0

    user_name = models.CharField(
        max_length=USER_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators= (
            validators.MinLengthValidator(USER_NAME_MIN_LEN),
            validator_only_alphanumeric_and_underscore,
        ),
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        validators = (
            validators.MinValueValidator(AGE_MIN_AGE),
        )
    )

class Album(models.Model):
    NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30

    PRICE_MIN_VALUE = 0.0

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HIP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RB_MUSIC, RB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HIP_MUSIC, HIP_HIP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True,
        null=False,
        blank=False,
    )
    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=MUSICS,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
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

    class Meta:
        ordering = ('pk',)