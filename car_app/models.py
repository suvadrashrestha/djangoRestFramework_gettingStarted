from django.db import models
# Create your models here.


class ShowroomList(models.Model):
    name=models.CharField(max_length=255)
    locaiton=models.CharField(max_length=255)
    website=models.URLField(max_length=255)
    def __str__(self):
        return self.name


class CarList(models.Model):
    showroom=models.ForeignKey(ShowroomList,on_delete=models.CASCADE,blank=True,null=True)
    price= models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True)
    name=models.CharField(max_length=255)
    cassinumber=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name

