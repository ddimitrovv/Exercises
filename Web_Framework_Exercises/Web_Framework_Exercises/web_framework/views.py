import random
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, logout, login

UserModel = get_user_model()


def index(request):
    suffix = random.randint(1, 1000)

    # Not a good idea:
    # UserModel.objects.create(...)

    # Good idea:
    user = UserModel.objects.create_user(
        username=f'user_{suffix}',
        password='1123QwER',
    )

    # other_user = UserModel.objects.get(username='other_user')
    context = {
        'user': user
    }
    return render(request, 'index.html', context)


def login_user(request):
    # Authentication
    user = authenticate(
        username='test_user',
        password='1123QwER'
    )

    # Authorization
    login(request, user)  # Does `request.user = user` + other stuff

    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')
