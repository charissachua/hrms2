from rest_framework import serializers

from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    phone = serializers.CharField()
    salutation = serializers.CharField()
    gender = serializers.CharField()

    class Meta:
        model = Employee
        fields = ['id', 'username', 'email','first_name','last_name','phone','salutation','gender']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)

        employee = Employee.objects.create(user=user, **validated_data)
        return employee

    def update(self, instance, validated_data):

        #look at https://stackoverflow.com/questions/29457630/extend-user-model-django-rest-framework-3-x-x
        # takes care of validation and exception
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance







class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'


class EmployeeFullDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeFullDetails
        fields = '__all__'






