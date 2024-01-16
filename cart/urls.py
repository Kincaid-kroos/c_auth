from django.urls import path
from .views import CartItemsCreateView, CartItemsLatestView, CartItemsListView

urlpatterns = [
    path('', CartItemsListView.as_view(), name='all_cart_items'),
    path('cartitems/', CartItemsCreateView.as_view(), name='create_cartitem'),
    path('latest/', CartItemsLatestView.as_view(), name='latest_items'),
    
    
]
