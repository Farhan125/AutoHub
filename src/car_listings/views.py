from django.shortcuts import render
from rest_framework import generics
from .models import CarListing
from .serializers import CarListingSerializer

class CarListingListCreateView(generics.ListCreateAPIView):
    queryset = CarListing.objects.all()
    serializer_class = CarListingSerializer
