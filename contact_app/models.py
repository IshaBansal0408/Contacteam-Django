from django.db import models

# Create your models here.


class Contact(models.Model):
    contactName = models.CharField(max_length=256)
    contactNo = models.CharField(max_length=10)
    contactImg = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.contactName
