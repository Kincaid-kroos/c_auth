from django.urls import path
from .views import CartItemsCreateView, CartItemsLatestView

urlpatterns = [
    path('cartitems/', CartItemsCreateView.as_view(), name='create_cartitem'),
    path('latest/', CartItemsLatestView.as_view(), name='latest_items')
    
]
