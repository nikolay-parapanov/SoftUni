from django.http import request
from django.shortcuts import render, redirect

from games_play.web.forms import ProfileCreateForm, GameCreateForm, GameEditForm, ProfileEditForm, ProfileDeleteForm
from games_play.web.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.get()  # give me a profile, if we don't have it will raise exception and return None
    except Profile.DoesNotExist as ex:
        return None


def home(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


def dashboard(request):
    profile = Profile.objects.first()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    profile = Profile.objects.first()
    if request.method == "GET":
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-game.html', context)


def details_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'game': game,
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context={
        'profile':profile,
        'form':form,
    }
    return render(request, 'edit-game.html',context)


def delete_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            Game.objects.filter(pk=pk).delete()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
        'game': game,
    }
    return render(request, 'delete-game.html', context)


def create_profile(request):
    if get_profile() is not None:
        return redirect('home')

    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    games_count = Game.objects.count()
    if games_count != 0:
        average_rating = (sum(g.rating for g in games))/games_count
    else:
        average_rating = 0.0
    context = {
        'profile':profile,
        'games_count':games_count,
        'average_rating':average_rating,
    }

    return render(request, 'details-profile.html',context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        'profile':profile,
        'form':form,
    }
    return render(request, 'edit-profile.html',context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            Game.objects.all().delete()
            Profile.objects.first().delete()

            return redirect('home')
    context={
        'profile':profile,
        'form': form
    }
    return render(request, 'delete-profile.html',context)
