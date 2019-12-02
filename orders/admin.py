from django.contrib import admin

# Register your models here.
from .models import Item, Toppings, OrderItem, Order

admin.site.register(Item)
admin.site.register(Toppings)
admin.site.register(OrderItem)
admin.site.register(Order)
