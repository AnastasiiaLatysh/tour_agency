from django.conf.urls import url

from tours import views

urlpatterns = [
    url('delete', views.Basket().delete_from_basket, name='delete_from_basket')
]
