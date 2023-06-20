'''
Serializers convert complex Django models to JSON objects, making data easy to read on the API. 
'''

# import serializers module from the rest_framework package 
from rest_framework import serializers
from .models import BootcampMembers


# class StudentSerializer inherits from ModelSerializer class and converts complex BootcampMembers model instances to and from JSON format, 
# which can be easily consumed by web APIs.
class StudentSerializer(serializers.ModelSerializer):

    # Meta class within the StudentSerializer class  is used to provide metadata about the StudentSerializer class, 
    # like which model to serialize and which fields to include in the serialized representation.
    class Meta:
        # the BootcampMembers model you want to serialize and the fields you want to add to the API
        # BootcampMembers model that the serializer should use to create the serialized representation. 
        # This means that the serializer will convert instances of the BootcampMembers model to and from JSON format.
        model = BootcampMembers
        # Below we specifies which fields from the BootcampMembers model should be included in the serialized representation. 
        # In this case, we need all fields of the model
        fields = ('__all__')


