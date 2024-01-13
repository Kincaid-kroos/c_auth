from rest_framework import generics
from .models import ReviewsItems
from .serializers import ReviewsSerializer

class ReviewsCreateView(generics.CreateAPIView):
    queryset = ReviewsItems.objects.all()
    serializer_class = ReviewsSerializer

