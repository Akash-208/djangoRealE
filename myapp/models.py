from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class realestate(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=150, default="")
    mail = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=200,default="")
    area = models.IntegerField(default=0)
    numofbedroom = models.IntegerField(default=0)
    numofbathrooms = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='images/',default='')

    def __str__(self):
        return self.title
    