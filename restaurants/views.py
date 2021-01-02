from django.shortcuts import render
from .models import Restaurant
from django.views.generic import ListView


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurants/restaurant_list.html'
    context_object_name = 'restaurants'


def RestaurantDetailView(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    comments = restaurant.comments.all()
    context = {
        'restaurant': restaurant,
        'comments': comments,
    }

    return render(request, 'restaurants/restaurant_detail.html', context)
