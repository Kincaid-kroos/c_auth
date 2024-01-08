from django.contrib import admin
from .models import ReviewsItems

@admin.register(ReviewsItems)
class ReviewssAdmin(admin.ModelAdmin):
    list_display = ['name', 'comments', 'date_created']
    search_fields = ['name', 'comments']
    list_filter = ['date_created']
