from django.db import models
import random
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.

def image():
	return random.choice(urls)

# menu item
class Item(models.Model):
	category = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	price = models.FloatField()
	description = models.TextField()
	url = models.CharField(max_length=1000)
	slug = models.SlugField(default="test")

	def __str__(self):
		return f"{self.category} - {self.name} - {self.price} -  {self.description}"

	def get_abs_url(self):
		return reverse("product", kwargs={
			'slug': self.slug
			})
	def get_add_to_cart_url(self):
		return reverse("add-to-cart", kwargs={
			'slug': self.slug
			})

	def get_remove_from_cart_url(self):
		return reverse("remove-from-cart", kwargs={
			'slug': self.slug
			})

#menu item added to the order
class OrderItem(models.Model):
	user= models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	quantity = models.IntegerField(default=1)
	def __str__(self):
		return f"{self.quantity} order of {self.item.name}"
	def get_final_price(self):
		return self.quantity * self.item.price

# shoping card
class Order(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)
	def __str__(self):
		return f"{self.user.username} - {self.items} - {self.start_date} - {self.ordered_date} - {self.ordered}"

	def get_total(self):
		total = 0
		for order_item in self.items.all():
			total += order_item.get_final_price()
		return total

# <form id="orders" action="{% url 'addToOrder' menu_item_id=item.id %}" method="post">             {% csrf_token %}             {% for topping in toppings %}                 <input type="checkbox" name="topping" value="{{topping.id}}"> {{topping.topping}} <br>             {% endfor %}             <input id="order" type="submit" value = "Add to Order" disabled=true>



		