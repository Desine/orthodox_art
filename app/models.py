from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=False)
    care = models.TextField(null=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_amount = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Type(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class ProductType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='types')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('product', 'type')

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sizes')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('product', 'size')

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('product', 'material')

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    url = models.URLField()
    
    def __str__(self):
        return f"Image for {self.product.name}"



class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    
    class Meta:
        unique_together = ('user', 'product')



class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    shipping_address = models.TextField()
    
    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product.name} in order #{self.order.id}"
    
    
    
    
    