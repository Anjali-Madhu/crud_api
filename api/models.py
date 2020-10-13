from django.db import models

# Create your models here.

class Product(models.Model):
    PRODUCT_TYPE = ((0,"Mobile"),(1,"Laptop"))
    name = models.TextField(max_length=200,null=False)
    description = models.TextField(max_length=500,null=False)
    ram = models.IntegerField(null=False)
    type = models.IntegerField(choices=PRODUCT_TYPE,null=False)
    processor = models.CharField(max_length=10,null=False)
