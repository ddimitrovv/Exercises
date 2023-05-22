from django.shortcuts import render, redirect

from Car_Collection_App.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, CarCreateForm, \
    CarEditForm, CarDeleteForm
from Car_Collection_App.web.models import Profile, Car


def get_profile():
    current_profile = Profile.objects.all() or None
    return current_profile


def get_cars():
    cars = Car.objects.all().order_by('pk')
    return cars


def get_car(pk):
    car = Car.objects.filter(pk=pk).get()
    return car


def index(request):
    current_profile = get_profile()

    context = {
        'profile': current_profile,
    }

    return render(
        request, 'base/index.html', context,
    )


def catalogue(request):
    profile = get_profile()
    cars = get_cars()

    context = {
        'profile': profile,
        'cars': cars
    }

    return render(request, 'base/catalogue.html', context)


def profile_create(request):
    current_profile = get_profile()
    if current_profile is not None:
        return redirect('catalogue')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    current_profile = Profile.objects.get()
    cars = get_cars()
    cars_total_price = sum([car.price for car in cars])

    context = {
        'cars_total_price': cars_total_price,
        'profile': current_profile
    }
    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    current_profile = Profile.objects.get()
    if request.method == "GET":
        form = ProfileEditForm(instance=current_profile)
    else:
        form = ProfileEditForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        'form': form
    }
    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    current_profile = Profile.objects.get()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=current_profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=current_profile)
        if form.is_valid():
            form.save()
            cars = Car.objects.all()
            cars.delete()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'profile/profile-delete.html', context)


def car_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    profile = get_profile()
    car = get_car(pk)

    context = {
        'profile': profile,
        'car': car
    }

    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    profile = get_profile()
    car = get_car(pk)

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'car': car,
        'form': form
    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    profile = get_profile()
    car = get_car(pk)

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'car': car,
        'form': form
    }

    return render(request, 'car/car-delete.html', context)
