from django.urls import path

from basket.basket import Basket
from tours.plane_tour import plane_tour
from tours.bus_tour import bus_tour
from tours.tour import tour
from tours.train_tour import train_tour
from user.user import user

urlpatterns = [
    path('login/', user.login, name=''),
    path('', tour.show_all_tours, name='all_tours'),
    path(r'basket/', Basket().add_to_basket, name='add_to_basket'),
    path(r'bus/',  bus_tour.show_all_tours, name='bus'),
    path(r'plane/', plane_tour.show_all_tours, name='plane'),
    path(r'train/', train_tour.show_all_tours, name='train'),
]
