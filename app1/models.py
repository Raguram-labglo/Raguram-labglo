from django.db import models

class detiles_form(models.Model):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    
