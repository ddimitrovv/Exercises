from django.urls import path
from Web_Framework_Exercises.web_framework.views import index, login_user, logout_user

urlpatterns = (
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
)
