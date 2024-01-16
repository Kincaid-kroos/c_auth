from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from .models import cartItems
from .serializers import cartItemsSerializer

class CartItemsCreateView(generics.CreateAPIView):
    queryset = cartItems.objects.all()
    serializer_class = cartItemsSerializer
    permission_classes = (permissions.AllowAny, )

class CartItemsListView(generics.ListAPIView):
    queryset = cartItems.objects.all()
    serializer_class = cartItemsSerializer
    permission_classes = (permissions.AllowAny, )    


class CartItemsLatestView(generics.ListAPIView):
    queryset = cartItems.objects.filter(latest=True).order_by('-date_created')
    serializer_class = cartItemsSerializer
    permission_classes = (permissions.AllowAny, )

