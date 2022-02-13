from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Stocks(models.Model):      
    name = models.CharField(max_length = 30)  
    ticker= models.CharField(max_length=30, null=True)
    stock_exchange=models.CharField(max_length=10, default="NSE")
    price=models.IntegerField(null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name  

    def get_stock_detail_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


