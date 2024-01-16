from django.urls import path
from .views import CarListingListCreateView

urlpatterns = [
    path('car-listings/', CarListingListCreateView.as_view(), name='car-listings'),
]
