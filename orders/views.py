from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Item, OrderItem, Order
from django.utils import timezone

class  homeView(ListView):
	model = Item
	paginate_by = 8
	template_name = "home_page.html"


class OrderSummaryView(LoginRequiredMixin,View):
	def get(self, *args, **kwargs):
		try:
			order = Order.objects.get(user=self.request.user, ordered=False)
			context = {
				'object': order
			}
			return render(self.request,'order_summary.html', context)
		except ObjectDoesNotExist:
			messages.error(self.request, "You do not have an active order")
			return redirect("/")
		
	
class itemDetailView(DetailView):
	model = Item
	template_name= "product_page.html"

def CheckoutView(request):
	context = {
		"items": Item.objects.all()
	}
	return render(request, "checkout_page.html", context)

@login_required
def add_to_cart(request, slug): 
	item = get_object_or_404(Item, slug=slug)  
	order_item, created= OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		#check of the order item is in the order 
		if order.items.filter(item__slug=item.slug).exists():
			order_item.quantity +=1
			order_item.save()
			messages.info(request, "This item quantity was updated.")
			return redirect("order-summary")
		else:
			order.items.add(order_item)
			messages.info(request, "This item was added to your cart.")
			return redirect("order-summary")
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(
			user=request.user, 
			ordered_date=ordered_date)
		order.items.add(order_item)
	return redirect('product', slug=slug)

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
    	order = order_qs[0]
    	# check if the order item is in the order
    	if order.items.filter(item__slug=item.slug).exists():
    		order_item = OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]
    		order.items.remove(order_item)
    		messages.info(request, "This item was removed from your cart.")
    		return redirect("order-summary")
    	else:
    		messages.info(request, "This item was not in your cart")
    		return redirect("product", slug=slug)
    else:
    	messages.info(request, "You do not have an active order")
    	return redirect("product", slug=slug)

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
    	order = order_qs[0]
    	# check if the order item is in the order
    	if order.items.filter(item__slug=item.slug).exists():
    		order_item = OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]
    		order_item.quantity -=1
    		order_item.save()
    		messages.info(request, "This item quantity was updated")
    		return redirect("order-summary")
    	else:
    		messages.info(request, "This item was not in your cart")
    		return redirect("product", slug=slug)
    else:
    	messages.info(request, "You do not have an active order")
    	return redirect("product", slug=slug)
