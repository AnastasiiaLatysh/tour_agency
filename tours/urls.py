from django.urls import path

from tours import views

urlpatterns = [
    path('', views.Tours.show_all_tours),
    path(r'order/', views.Tours.order_tour, name='order'),
    path(r'basket/', views.Tours.add_to_basket, name='add_to_basket'),
]
