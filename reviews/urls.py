from django.urls import path
from .views import ReviewsCreateView

urlpatterns = [
    path('post/', ReviewsCreateView.as_view(), name='create_review'),
    
]
