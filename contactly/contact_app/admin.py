from django.contrib import admin
from contact_app import models
# Register your models here.
admin.site.register([
    models.Contact
])
