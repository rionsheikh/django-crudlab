from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=120,verbose_name="Product Title")
    sku=models.CharField(max_length=50,unique=True,verbose_name="Product Code")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Retail Price")
    stock_quantity=models.IntegerField(verbose_name="Units in Stock")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"