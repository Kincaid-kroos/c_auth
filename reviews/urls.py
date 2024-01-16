from django.urls import path
from .views import ReviewsCreateView
from .views import ReviewsView

urlpatterns = [
    path('', ReviewsView.as_view(), name='reviews'),
    path('post/', ReviewsCreateView.as_view(), name='create_review'),
    
]
