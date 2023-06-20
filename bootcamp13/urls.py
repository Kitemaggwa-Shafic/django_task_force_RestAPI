from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name = 'home'),
    path('all_students/', views.all_students),
 
]