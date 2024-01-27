from django.contrib import admin
from .models import cartItems

@admin.register(cartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'amount', 'latest', 'date_created','available']
    search_fields = ['name']
    list_filter = ['latest', 'date_created']
    list_editable = ['amount', 'latest','available']
    date_hierarchy = 'date_created'
