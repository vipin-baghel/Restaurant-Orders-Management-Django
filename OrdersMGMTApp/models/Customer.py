from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()

    def validate_phone(self):
        error_msg = None
        if len(str(self.phone)) != 10:
            error_msg = 'Phone number should be of 10 digits'
        return error_msg

    def validate_name(self):
        error_msg = None
        if len(str(self.name)) < 2:
            error_msg = 'Please provide name'
        return error_msg

    def __str__(self):
        return self.name



