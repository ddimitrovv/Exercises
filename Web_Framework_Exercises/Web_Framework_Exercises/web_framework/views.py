import random
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login

UserModel = get_user_model()


def index(request):
    return render(request, 'index.html')


def login_user(request):
    suffix = random.randint(1, 1000)

    # Authentication
    user = authenticate(
        username='test_user',
        password='1123QwER'
    )

    # Authorization
    login(request, user)  # request.user = user + other staff

    context = {
        'user': user
    }

    return render(request, 'login.html', context)
