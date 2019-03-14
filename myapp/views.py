from django.shortcuts import render, get_object_or_404
from .models import Dish, Restaurant
from .forms import DishForm, RestaurantForm
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView
)
from .serializer import RestaurantCreateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

class RestaurantCreate(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer

class RestaurantListApi(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer

class RestaurantDetailApi(APIView):
    def get(self,request,id):
        data = Restaurant.objects.get(id=id)
        serializer = RestaurantCreateSerializer(data)
        return Response(serializer.data)


class Sample(TemplateView):
    template_name = "myapp/home.html"

class AddRestaurant(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    # success_url = "/myapp/home"
    template_name = "myapp/restaurant_form.html"

class UpdateRestaurant(UpdateView):
    model = Restaurant    
    form_class = RestaurantForm

class ListRestaurant(ListView):
    model = Restaurant
    paginate_by = 2
    ordering = 'name'

class RestaurantDetail(DetailView):
    model = Restaurant
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Restaurant,id=id_)

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail,self).get_context_data(**kwargs)
        print(context)
        qs1 = Dish.objects.filter(restaurant_name=context['object'].id)
        context.update({
			'dish' : qs1,
			})
        return context

class DeleteDish(DeleteView):
    model = Dish
    success_url = "/myapp/"