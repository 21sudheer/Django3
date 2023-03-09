from django.urls import path
from jan import views

urlpatterns=[
    path('first/',views.first, name='first')
]