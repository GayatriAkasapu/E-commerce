from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem, Cart, CartItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)

