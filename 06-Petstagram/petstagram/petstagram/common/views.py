import pyperclip
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse

from petstagram.common.forms import PhotoCommentForm, SearchPhotosForm
from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_user_liked_photos, get_photo_url
from petstagram.core.utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo


def index(request):
    search_form = SearchPhotosForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()

    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)

    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    print(photos)
    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }

    return render(
        request,
        'common/home-page.html',
        context,
    )


@login_required
def like_photo(request, photo_id):
    user_liked_photos = PhotoLike.objects\
        .filter(photo_id=photo_id,user_id=request.user.pk)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # Variant 1
        # photo_like = PhotoLike(
        #     photo_id=photo_id,
        # )
        # photo_like.save()

    # # Variant 2
        PhotoLike.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )
    redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    return redirect(redirect_path)

def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk':photo_id
    })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request,photo_id))


