from django.urls import path
from calc import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('details',views.details, name='details'),
    path('update/<int:i>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('testing/', views.testing, name='testing'),
    path('block/', views.block, name='block'),
    path('comment/', views.comment, name='comment'),
    path('cycle/', views.cycle, name='cycle')
]