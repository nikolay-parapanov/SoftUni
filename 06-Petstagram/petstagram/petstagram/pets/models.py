from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    PET_MAX_NAME = 30
    name = models.CharField(
        max_length=PET_MAX_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # def __init__(self, *args, **kwargs):
    #     if not self.slug:
    #         slug = slugify(f'{self.id}-{self.name}')
    #     super().__init__(slug=slug, *args, **kwargs)
    #
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.slug:
    #         self.slug = slugify(f'{self.id}-{self.name}')
    #
    #     return super().save(*args, **kwargs)
