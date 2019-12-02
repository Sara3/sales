from django.urls import path
from .views import (
    homeView, 
    CheckoutView,
    itemDetailView,
    OrderSummaryView,
    add_to_cart
)

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout', CheckoutView, name='checkout'),
    path('product/<slug>/', itemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart')
]
