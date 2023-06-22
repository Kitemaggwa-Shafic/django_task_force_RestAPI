'''
Serializers convert complex Django models to JSON objects, making data easy to read on the API. 
'''
# import serializers module from the rest_framework package 
from rest_framework import serializers
from .models import BootcampMembers


# class StudentSerializer inherits from ModelSerializer class from Django rest framework
class StudentSerializer(serializers.ModelSerializer):

    # Meta class provides metadata about the StudentSerializer class, 
     class Meta:
        # model attribute specifies what django model to work on. 
        model = BootcampMembers
        # field attribute specfies which field you need and we need all
        fields = ('__all__')
