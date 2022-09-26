from django.db import models

class Student(models.Model):

    name = models.CharField(max_length = 20)
    roll_no = models.IntegerField()
    profile = models.ImageField(upload_to = "images/", null=True)
    
    def __str__(self):
    	return "{}".format(self.id)
    
    
class Mark(models.Model):
    
    student_num = models.ForeignKey(Student, null = True, on_delete = models.CASCADE)
    M1 = models.IntegerField()
    M2 = models.IntegerField()
    M3 = models.IntegerField()
    M4 = models.IntegerField()
    M5 = models.IntegerField()
    
    def __str__(self):
    	return "{}".format(self.student_num)    
