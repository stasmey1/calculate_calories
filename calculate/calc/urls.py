from django.urls import path
from .views import *

urlpatterns = [
    path('', profile_list, name='profile_list'),
    path('profile_add/', profile_add, name='profile_add'),
    path('profile/<slug:slug>/', profile_ditail, name='profile'),
    path('profile_change/<slug:slug>/', profile_change, name='profile_change'),
    path('profile_delete/<slug:slug>/', profile_delete, name='profile_delete'),
]
