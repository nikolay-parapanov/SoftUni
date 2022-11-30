from django.shortcuts import render
from petstagram.core.utils import apply_likes_count, apply_user_liked_photo
from petstagram.pets.models import Pet


# Create your views here.
def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def delete_pet(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')


def get_pet_by_name_and_username(pet_slug, username):
    # TODO: fix when user auth
    return Pet.objects.get(slug=pet_slug)


def details_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': pet.photo_set.all(),
    }
    return render(
        request,
        'pets/pet-details-page.html',
        context
    )


def edit_pet(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')
