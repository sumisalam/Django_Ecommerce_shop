from django.db import models
from userapp.models import*

# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    img=models.FileField(upload_to='products')



