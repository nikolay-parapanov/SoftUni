from django.shortcuts import render, redirect
from petstagram.core.utils import apply_likes_count, apply_user_liked_photo, is_owner
from petstagram.pets.forms import PetCreateForm, PetDeleteForm, PetEditForm
from petstagram.pets.models import Pet


def get_pet_by_name_and_username(pet_slug, username):
    return Pet.objects.get(slug=pet_slug, user__username=username)


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


def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        # request.method =='POST'
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }

    return render(request, 'pets/pet-delete-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)

    if not is_owner(request, pet):
        return redirect('details pet', username=username, pet_slug=pet_slug)

    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }

    return render(request, 'pets/pet-edit-page.html', context)
