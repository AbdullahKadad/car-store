from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('cars', CarsListView.as_view(), name="car_list"),
    path('<int:pk>/car_detail', CarDetailView.as_view(), name="car_detail"),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('create', CarCreateView.as_view(), name='car_create'),
]