from django.contrib import admin
from .models import ReviewsItems

@admin.register(ReviewsItems)
class ReviewssAdmin(admin.ModelAdmin):
    list_display = ['name', 'comments']
    search_fields = ['name', 'comments']
    
