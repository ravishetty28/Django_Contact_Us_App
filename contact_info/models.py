from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False)
    address = models.TextField()
    pin = models.IntegerField()

    def __str__(self):
        return self.first_name