from django.db import models


# Create your models here.
class Attendence(models.Model):
	userid=models.CharField(max_length=20) 
	date=models.DateTimeField()
	checktime=models.DateTimeField() 



def __str__(self):
	return self.userid
