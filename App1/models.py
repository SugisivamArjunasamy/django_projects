from django.db import models
from django.utils.timezone import now

class Product(models.Model):
   name = models.CharField(max_length=150,default="")
   code = models.CharField(max_length=150,default="")
   studio = models.CharField(max_length=150,default="")
   deliveryDate = models.DateTimeField(default=now())
   thumbnail = models.CharField(max_length= 250,default="")
   img1 = models.CharField(max_length= 250,default="")
   img2 = models.CharField(max_length= 250,default="")
   img3 = models.CharField(max_length= 250,default="")
   price = models.CharField(max_length= 150,default="")
  
class User(models.Model):  
   username = models.CharField(max_length= 150)  
   password = models.CharField(max_length= 250)


   