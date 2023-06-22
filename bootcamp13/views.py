from django.shortcuts import render
from .models import *

from .serializer import StudentSerializer
from rest_framework.response import Response
# The @api_view decorator shows a view function can handle HTTP GET requests.
from rest_framework.decorators import api_view 

# Create your views here.
def home(request):
    members = BootcampMembers.objects.all()
    context = {"members": members}
    return render(request, "home.html", context)


@api_view(["GET"])
def all_students(request):
    # retrieves all instances of BootCampMembers from db
    members = BootcampMembers.objects.all() 
    serializer = StudentSerializer(members, many=True)
    # this helps return the data back to the UI in appropriate format
    return Response(serializer.data)


# Update student function using pk constratint
@api_view(["PUT"])
def UpdateStudent(request, pk):
    # This method retrieves a single instance of the student model with the given primary key pk.
    student = BootcampMembers.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Student Updated Successfully !!!")


# delete student rest funstion basing on pk
@api_view(["DELETE"])
def DeleteStudent(request, pk):
    deletestudent = BootcampMembers.objects.get(id=pk)
    deletestudent.delete()
    return Response("Student deleted successfuly !!")


# Function for creating new student
@api_view(["POST"])
def new_student(request):
    # serializer variable gets data from StudentSerializer class and the pass data from the UI
    serializer = StudentSerializer(data=request.data)
    # Checking if the data sent is valid be4 saving the data
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Function to return a student basing on id
@api_view(["GET"])
def ViewStudent(request, pk):
    selectedStudent = BootcampMembers.objects.get(id=pk)
    serializer = StudentSerializer(selectedStudent)
    return Response(serializer.data)