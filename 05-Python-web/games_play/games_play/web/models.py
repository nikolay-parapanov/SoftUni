from django.core import validators
from django.core import exceptions
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LEN =30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    email= models.EmailField(
        null=False,
        blank=False,
    )

    age= models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(AGE_MIN_VALUE),
        ),
    )

    password = models.CharField(
        max_length= PASSWORD_MAX_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name and not self.last_name:
            return f'{self.first_name}'
        if not self.first_name and self.last_name:
            return f'{self.last_name}'
        if not self.first_name and not self.last_name:
            return None

    full_name_for_form = full_name

class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0
    MAX_LEVEL_MIN_VALUE = 1

    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"

    CATS = (
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER),
    )

    title= models.CharField(
        max_length= TITLE_MAX_LEN,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CATS,
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(RATING_MIN_VALUE),
            validators.MaxValueValidator(RATING_MAX_VALUE),
        ),
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            validators.MinValueValidator(MAX_LEVEL_MIN_VALUE),
        ),
    )
    image_url= models.URLField(
        null=False,
        blank=False,
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )


