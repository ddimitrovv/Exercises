import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

# from Web_Framework_Exercises.web_framework.forms import ProfileForm
from Web_Framework_Exercises.web_framework.models import CustomUser

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


# def login_user(request):
#     # Authentication
#     user = authenticate(
#         username='test_user',
#         password='1123QwER'
#     )
#
#     # Authorization
#     login(request, user)  # Does `request.user = user` + other stuff
#
#     return redirect('index')

class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')


class CreateProfileView(CreateView):
    model = CustomUser
    fields = ['username', 'password']
    template_name = 'create_profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Hash the password before saving the user
        form.instance.set_password(form.cleaned_data['password'])
        return super().form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Return the profile associated with the currently logged-in user
        return self.request.user
