import random
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()


def login_user(request):
    suffix = random.randint(1, 1000)

    user = authenticate(
        username='test_user',
        password='1123QwER'
    )

    context = {
        'user': user
    }

    return render(request, 'index.html', context)
