from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=2082)
    size =models.IntegerField()
   


    def __str__(self):
      return self.name
    


class Orderdetail(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
  product= models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
 



  # def total_price(self):
  #     return self.quantity * self.product.price
  #   total_price = property(total_price)

  # def __str__(self):
  #    return self.user.username





# class Order(models.Model):
#   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
#   orderdate = models.DateTimeField(blank=True, null=True)

  
#   def __str__(self):
#     return self.user.username


