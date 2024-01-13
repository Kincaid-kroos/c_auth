from rest_framework import serializers
from .models import ReviewsItems

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsItems
        fields = '__all__'