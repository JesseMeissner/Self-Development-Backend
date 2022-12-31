from django.shortcuts import render
from rest_framework import generics
from .models import Reviews
from .serializers import ReviewsSerializer

# Create your views here.
class ReviewsList(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer