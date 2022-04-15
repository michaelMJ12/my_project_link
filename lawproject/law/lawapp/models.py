from django.db import models
from django.core.validators import RegexValidator






class Appointment(models.Model):
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField( max_length=100, blank=True,null=True)
    email = models.EmailField(null=True, max_length=50)
    address = models.CharField(max_length=50, null=True)
    messages = models.TextField(max_length=50, null=True)





class Consultant(models.Model):
    # phone_regexC = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    nameC = models.CharField(max_length=50, null=True)
    phoneC = models.CharField( max_length=100, blank=True,null=True)
    emailC = models.EmailField(null=True, max_length=50 )
    addressC = models.CharField(max_length=50, null=True)
    messagesC = models.TextField(max_length=50, null=True)


class Message(models.Model):
    # phone_regexM = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    nameM = models.CharField(max_length=50, null=True)
    phoneM = models.CharField(  max_length=100, blank=True,null=True)
    emailM = models.EmailField(null=True, max_length=50)
    # addressC = models.CharField(max_length=50, null=True)
    messagesM = models.TextField(max_length=50, null=True)
