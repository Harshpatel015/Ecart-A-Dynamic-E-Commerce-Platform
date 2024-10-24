from django.db import models
from django.utils import timezone

class ProductCategory(models.Model):
    product_category_name = models.CharField(max_length=50)
    product_category_image = models.ImageField(upload_to="product_category", null=True, blank=True)

    def __str__(self):
        return self.product_category_name


class ProductSubCategory(models.Model):
    product_sub_category_name = models.CharField(max_length=50)
    product_sub_category_image = models.ImageField(upload_to="product_sub_category", null=True, blank=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_sub_category_name


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    product_sub_category = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="product_photos", null=False, blank=False)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_listing_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name
    
    
class shipping_address(models.Model):
    
    Contact_Person_Name = models.CharField(max_length=150)
    Contact_Person_phone_number = models.IntegerField(max_length=10)
    Contact_Person_Email = models.EmailField(max_length=254,default="")
    Street_Address = models.CharField(max_length = 500 )
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)