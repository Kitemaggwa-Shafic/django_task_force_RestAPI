from django.db import models

# Create your models here.
class BootcampMembers(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    # Was proposing we add on some of these fields too 
    #1 gender = models.CharField(max_length=10) 
    #2 email_address = models.EmailField()
    #3 phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.fName+''+ self.lName
 
