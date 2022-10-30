from django.shortcuts import render, redirect

from car_collection_app.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from car_collection_app.web.models import Profile, Car

def index(request):
    profile = Profile.objects.first()

    context = {
        'profile':profile,
    }
    return render(request, 'index.html',context)

def profile_create(request):
    profile = Profile.objects.first()
    if profile:
        return redirect('index')

    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form':form,
    }
    return render(request, 'profile-create.html',context)

def catalogue(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    total_cars = len(cars)

    context = {
        'profile':profile,
        'cars':cars,
        'total_cars':total_cars,
    }
    return render(request, 'catalogue.html', context)

def car_create(request):
    profile = Profile.objects.first()
    if request.method =="GET":
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form':form
    }
    return render(request, 'car-create.html',context)

def car_details(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.filter(pk=pk).get()
    context = {
        'profile':profile,
        'car':car
    }
    return render(request, 'car-details.html',context)

def car_edit(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context={
        'profile':profile,
        'car':car,
        'form':form,
    }
    return render(request, 'car-edit.html',context)

def car_delete(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context={
        'profile':profile,
        'car':car,
        'form':form,
    }
    return render(request, 'car-delete.html',context)

def profile_details(request):
    profile = Profile.objects.first()
    if Car.objects.all():
        cars = Car.objects.all()
        total_price = sum(c.price for c in cars)
    else:
        cars = 0
        total_price = 0
    context={
        'profile':profile,
        'total_price':total_price,
    }
    return render(request, 'profile-details.html',context)

def profile_edit(request):
    profile = Profile.objects.first()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile':profile,
    }
    return render(request, 'profile-delete.html',context)


