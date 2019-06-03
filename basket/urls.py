from django.urls import path

from basket.basket import Basket

urlpatterns = [
    path(r'delete', Basket().delete_from_basket, name='delete_from_basket'),
    path(r'order/', Basket().order_tour, name='order'),
]
