from django.db import models

# Create your models here.

class Category(models.Model):
    image = models.FileField(null=True,blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    publication_status = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class Manufacturer(models.Model):
    image = models.FileField(null=True,blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    publication_status = models.BooleanField()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    details = models.TextField()
    price = models.SmallIntegerField()
    quantity = models.SmallIntegerField()
    stock_label = models.SmallIntegerField()
    image = models.FileField(null=True,blank=True)
    publication_status = models.BooleanField()
    
    def __str__(self):
        return self.name
    

'''
proposed table_list
--------------------
category_id
name
slug
publication_status

same as manufacturer

product
product_id
catefory_id
manufacturer_id
name
price
quantity
image
stock_label
publication_status
'''