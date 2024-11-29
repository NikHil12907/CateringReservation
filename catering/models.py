from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=100, default='Snacks')
    
    def __str__(self):        
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product.name} - {self.quantity}x"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    preferences = models.TextField(blank=True, null=True)
    
    def __str__(self) :
        return f"{self.user.username}'s profile"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock', 'category']
        
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is None or stock < 0:
            return 0
        return stock
    
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number','address', 'email', 'preferences'] 