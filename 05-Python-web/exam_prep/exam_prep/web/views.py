from django.shortcuts import render, redirect

from exam_prep.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from exam_prep.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get() #give me a profile, if we don't have it will raise exception and return None
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    context = {
        'albums': Album.objects.all()
    }
    return render(request, 'core/home-with-profile.html', context)


def add_album(request):
    if request.method== "GET":
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form':form,
    }
    return render(request, 'albums/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context ={
        'album': album,
    }
    return render(request, 'albums/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method =="GET":
        form = AlbumEditForm(instance=album)    # with this we pre-populate the Form details
    else:
        form = AlbumEditForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context= {
        'form': form,
        'album':album,                          # because of the URL we have to add the album in the context
    }
    return render(request, 'albums/edit-album.html',context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method=="GET":
        form = AlbumDeleteForm(instance=album)
    else:
        # Album.objects.filter(pk=pk).delete()        # Don't delete it this way, as you won't be able to catch the validation in the Form. It's not abstract way. Deletion should be done in the Form!!!
        form = AlbumDeleteForm(instance=album)
        if form.is_valid():
            #todo: delete
            return  redirect('index')

        context={
            'form': form,
            'album':album,
        }
    return render(request, 'albums/delete-album.html')


def details_profile(request):
    return render(request, 'profile/profile-details.html')


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')

def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()  #Here we create empty form
    else:
        form = ProfileCreateForm(request.POST)   #here somthing is sent to the form. Find out what's sent
        if form.is_valid():                     # is it valid
            form.save()                         #if yes save it
            return redirect('index')

    context= {                                  #if not valid...
        'form':form,
    }
    return render(request, 'core/home-no-profile.html', context,)