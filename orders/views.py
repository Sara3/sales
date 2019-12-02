from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Item, Toppings, OrderItem, Order
from django.utils import timezone

class  homeView(ListView):
	model = Item
	paginate_by = 6
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
	item = get_object_or_404(Item, slug=slug, id=1)
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
		else:
			order.items.add(order_item)
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(
			user=request.user, 
			ordered_date=ordered_date)
		order.items.add(order_item)
	return redirect('product', slug=slug)