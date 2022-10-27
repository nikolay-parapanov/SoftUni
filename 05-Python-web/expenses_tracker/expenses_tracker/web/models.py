from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = "Ensure this value contains only letters."


def validator_only_letters(value):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)


@deconstructible
class MaxFileSizeInMBValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f"Max file size is {self.max_size:.2d} MB"


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15

    BUDGET_DEFAULT = 0
    BUDGET_MIN_START = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validator_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validator_only_letters,
        )
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT,
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(BUDGET_MIN_START),
        )

    )
    image = models.URLField(
        # upload_to=IMAGE_UPLOAD_TO_DIR,
        # default='staticfiles/images/user.png',
        null=True,
        blank=True,
    )


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

'''•	Expense
o	Title
    	Character field, required.
    	It should consist of a maximum of 30 characters.
o	Expense Image
	    URL field, required.
o	Description
	    Text field, optional.
o	Price
	    Float field, required.

'''


class Expense(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
        blank=False,
    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )
