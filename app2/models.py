from django.db import models

class Department(models.Model):

    name = models.CharField(max_length = 20)
    class Meta:
        ordering = ['name']

   
    def __str__(self):
       
        return self.name
   

class Posting(models.Model):

    post = models.CharField(max_length = 50, null=True)
    
    def __str__(self):
        return self.position
   
   
class Employee(models.Model):

    name = models.CharField(max_length = 20)
    age = models.IntegerField(null=True)
    department = models.ManyToManyField(Department)
    position = models.ForeignKey(Posting,null =True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
