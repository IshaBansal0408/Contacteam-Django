from django.contrib import admin
from emp_app import models
# Register your models here.
admin.site.register([
    models.Employee,
    models.Department,
    models.Role
])
