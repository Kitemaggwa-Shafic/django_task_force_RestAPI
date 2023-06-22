from django.db import models


# Create your models here.

# Course model of students
class Course(models.Model):
    courseName = models.CharField(max_length=100)
    def __str__(self):
        return self.courseName


# BootcampMembers models
class BootcampMembers(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #  __str__ method, you can customize how the object is represented as a string.  
    # it will return the full name of the object by concatenating the fName and lName attributes
    def __str__(self):
        return self.fName + " " + self.lName
