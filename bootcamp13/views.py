from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    members = BootcampMembers.objects.all()
    context = {
        'members':members
    }
    return render(request, 'home.html', context)