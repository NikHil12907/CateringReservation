from django.contrib import admin
from .models import Product, Order, Cart, UserProfile
# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(UserProfile)