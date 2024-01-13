from rest_framework import serializers
from .models import cartItems

class cartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartItems
        fields = '__all__'