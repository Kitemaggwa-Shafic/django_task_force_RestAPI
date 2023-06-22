from django.urls import path
from . import views
from .views import *

urlpatterns = [ 
    path('', views.home, name = 'home'),
    path('all_students/', views.all_students),  
    path('update_student/<int:pk>/', views.UpdateStudent),
    path('delete_student/<int:pk>/', views.DeleteStudent),
    # as_view() converts a class into a callable function
    path('new_student/', NewStudent.as_view() ),
    path('new_course/', views.create_course), 

]