from django.urls import path
from .views import RestaurantListView, RestaurantDetailView

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant-list'),
    path('<int:pk>', RestaurantDetailView, name='restaurant-detail'),
]
