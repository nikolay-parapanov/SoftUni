from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


# Create your views here.



def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo

def apply_user_liked_photo(photo):
    #TODO: fix this for current user when authentication is available
    photo.is_liked_by_user = photo.likes_count>0
    return photo

def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html')

def like_photo(request, photo_id):
    #Variant 1
    photo_like = PhotoLike(
        photo_id = photo_id,
    )
    photo_like.save()

    #Variant 2
    PhotoLike.objects.create(
        photo_id= photo_id,
    )

    redirect_path = request.META['HHTP_REFERER']+f'#photo-{photo_id}'

    return redirect(redirect_path)