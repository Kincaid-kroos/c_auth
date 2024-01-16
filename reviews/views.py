from rest_framework import generics
from .models import ReviewsItems
from rest_framework import permissions
from .serializers import ReviewsSerializer

class ReviewsCreateView(generics.CreateAPIView):
    queryset = ReviewsItems.objects.all()
    serializer_class = ReviewsSerializer

class ReviewsView(generics.ListAPIView):
    queryset = ReviewsItems.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = (permissions.AllowAny, )

    