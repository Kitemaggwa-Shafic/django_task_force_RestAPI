from django.shortcuts import render
from .models import *

# 
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

def home(request):
    members = BootcampMembers.objects.all()
    context = {
        'members':members
    }
    return render(request, 'home.html', context)

#  Was proposing we change it function to return all students like this

# The @api_view decorator shows a view function only accessed via HTTP GET requests.
@api_view(['GET']) 
# This function takes a HTTP client request parameter.
def all_students(request):
    members = BootcampMembers.objects.all()
    serializer = StudentSerializer(members, many = True)
    return Response(serializer.data)

