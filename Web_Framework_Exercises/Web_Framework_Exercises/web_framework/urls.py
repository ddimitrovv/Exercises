from django.contrib.auth.views import LoginView
from django.urls import path
from Web_Framework_Exercises.web_framework.views import index, logout_user, CreateProfileView, CustomLoginView, \
    UserDetailView

urlpatterns = (
    path('', index, name='index'),
    # path('login/', login_user, name='login'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('create/', CreateProfileView.as_view(), name='create profile'),
    path('details/', UserDetailView.as_view(), name='details profile'),
)
