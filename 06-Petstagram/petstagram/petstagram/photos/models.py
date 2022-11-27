from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet, StrFromFieldsMixin


# Create your models here.

def validate_image_less_than_5mb(image):
    filesize = image.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit *1024 *1024:
        raise ValidationError(f'Max filesize is {megabyte_limit} MB')

class Photo(StrFromFieldsMixin ,models.Model):
    str_fields = ('photo', 'location')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',
        null=False,
        blank=True,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    location= models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )