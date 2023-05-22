from django.urls import path, include
from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile create'),
        path('details/', views.profile_details, name='profile details'),
        path('edit/', views.profile_edit, name='profile edit'),
        path('delete/', views.profile_delete, name='profile delete'),
    ])),
    path('car/', include([
        path('create/', views.car_create, name='car create'),
        path('<int:pk>/details/', views.car_details, name='car details'),
        path('<int:pk>/edit/', views.car_edit, name='car edit'),
        path('<int:pk>/delete/', views.car_delete, name='car delete'),
    ])),
)


