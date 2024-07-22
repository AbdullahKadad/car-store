from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import *
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class CarsListView(ListView):
    template_name = 'car_list.html'
    model = Car
    context_object_name = 'car'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    fields = ['model', 'brand', 'price', 'is_bought', 'buy_time']
    template_name = 'car_update.html'
    success_url = reverse_lazy('car_list')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    def get_success_url(self):
        return reverse('car_list')
    
class CarCreateView(CreateView):
    model = Car
    fields = ['buyer_id', 'model', 'brand', 'price', 'is_bought', 'buy_time']
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')