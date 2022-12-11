from django.db import models
from django.conf import settings
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name + " - " + self.location


class Role(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Employee(models.Model):
    GENDER = (("F", "Female"), ("M", "Male"), ("U", "Undisclosed"))
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True)
    # birth_date = models.DateField(blank=True)
    gender = models.CharField(choices=GENDER, max_length=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phoneNo = models.CharField(max_length=10)
    hire_date = models.DateField()
    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
