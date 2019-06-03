from django.urls import path

from basket.basket import Basket
from tours.plane_tour import PlaneTour
from tours.tour import Tour
from tours.bus_tour import BusTour
from tours.train_tour import TrainTour

urlpatterns = [
    path('', Tour().show_all_tours, name=''),
    path(r'basket/', Basket().add_to_basket, name='add_to_basket'),
    path(r'bus/', BusTour().show_all_tours, name='bus'),
    path(r'plane/', PlaneTour().show_all_tours, name='plane'),
    path(r'train/', TrainTour().show_all_tours, name='train')
]
