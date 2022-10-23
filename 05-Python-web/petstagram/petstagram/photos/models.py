#Photos / model.py
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_image_less_than_5MB

'''
The field Photo is required:
•	Photo - the user can upload a picture from storage, the maximum size of the photo can be 5MB
The fields description and tagged pets are optional:
•	Description - a user can write any description of the photo; it should consist of a maximum of 300 characters and a minimum of 10 characters
•	Location - it should consist of a maximum of 30 characters
•	Tagged Pets - the user can tag none, one, or many of all pets. There is no limit on the number of tagged pets
There should be created one more field that will be automatically generated:
•	Date of publication - when a picture is added or edited, the date of publication is automatically generated
'''

class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH= 10
    MAX_DESCRIPTION_LENGTH= 300
    MAX_LOCATION_LENGTH= 30

    # Requires media files to work correctly
    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',
        null=False,
        blank=True,
        validators=[validate_image_less_than_5MB],
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            # Django/ Python validation, not DB validation
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True, #Automatically sents current date on 'save' (update or create)
        null=False,
        blank=True,
    )

    # One - to - One
    # One - to - Many
    # Many - to Many

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
