from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name = 'home'),
    path('all_students/', views.all_students),  
    path('update_student/<int:pk>/', views.UpdateStudent),
    path('delete_student/<int:pk>/', views.DeleteStudent),
    path('new_student/', views.new_student),
 
]