from django.db import models
from adminapp.models import*

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    role = models.CharField(max_length=100)

class register(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    email = models.CharField(max_length=260)
    phono = models.BigIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    log=models.ForeignKey(login,on_delete=models.CASCADE)


class orders1(models.Model):
    img=models.FileField(upload_to='orders')

    product=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    quantity=models.IntegerField()
    pri=models.FloatField()

    uid=models.ForeignKey(register,on_delete=models.CASCADE)
    pid=models.ForeignKey(products,on_delete=models.CASCADE)

class orders3(models.Model):

    img=models.FileField(upload_to='orders2')

    product=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    quantity=models.IntegerField()
    pri=models.FloatField()

    uid=models.ForeignKey(register,on_delete=models.CASCADE)
    pid=models.ForeignKey(products,on_delete=models.CASCADE)



class paym(models.Model):


   cardname=models.CharField(max_length=100)
   cardnumber=models.CharField(max_length=100)
   subtotal=models.FloatField()
   uid = models.ForeignKey(register, on_delete=models.CASCADE)






