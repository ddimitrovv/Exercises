from django.shortcuts import render, redirect

from Car_Collection_App.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from Car_Collection_App.web.models import Profile, Car


def get_profile():
    current_profile = Profile.objects.all() or None
    return current_profile


def index(request):
    current_profile = get_profile()

    context = {
        'profile': current_profile,
    }

    return render(
        request, 'base/index.html', context,
    )


def catalogue(request):
    return render(request, 'base/catalogue.html')


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
    cars_total_price = 0
    # TODO: total price of the cars

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
            # TODO: when cars uncomment lines below
            # cars = Car.objects.all()
            # cars.delete()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'profile/profile-delete.html', context)


def car_create(request):
    return render(request, 'car/car-create.html')


def car_details(request, pk):
    return render(request, 'car/car-details.html')


def car_edit(request, pk):
    return render(request, 'car/car-edit.html')


def car_delete(request, pk):
    return render(request, 'car/car-delete.html')
