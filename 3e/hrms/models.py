# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Country(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Location(models.Model):
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state_province = models.CharField(max_length=45)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Department(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class JobTitle(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    GENDER = (('F', 'female'), ('M', 'male'))
    SALUTATION = models.TextChoices('Mr','Mrs')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salutation = models.CharField(max_length=45, choices=SALUTATION.choices)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=45, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)



class DeptEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class EmployeeManager(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee')
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='manager')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class EmployeeJobTitle(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    jobtitle = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    start_date = models.DateField()
    confirm_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class EmployeeDetails(models.Model):
    salutation = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=45)
    is_superuser = models.CharField(max_length=1)
    picture = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField()
    user_id = models.IntegerField(null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'employee_details'


class EmployeeFullDetails(models.Model):
    salutation = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=45)
    picture = models.CharField(max_length=100, blank=True, null=True)
    mgr_id = models.IntegerField()
    mgr_fname = models.CharField(max_length=45)
    mgr_lname = models.CharField(max_length=45)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_title = models.CharField(max_length=100)
    dept_name = models.CharField(max_length=45)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'employee_full_details'
