from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.member, name='member'),
    path('members/details/<int:id>', views.details, name='details'),
    path('forms/', views.form, name='form')
    
]