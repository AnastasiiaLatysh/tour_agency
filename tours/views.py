# from django.db import connection
#
# # Create your views here.
# # from tours.models import Tours
#
#
# from django.shortcuts import render
#
# from basket.views import Basket
# from tours.forms import OrderTourForm
#
# cursor = connection.cursor()
#
#
# class Tours(object):
#
#     @staticmethod
#     def show_all_tours(request):
#         cursor.execute("SELECT nname, price, available_seats FROM tours WHERE available_seats > 0")
#         tours = []
#         for row in cursor.fetchall():
#             tours.append(row)
#         context = {'tours': tours}
#         return render(request, "all_tours.html", context)
#
#     @staticmethod
#     def order_tour(request):
#         tour_name = request.GET.get('tour_name')
#         form = OrderTourForm(initial={'tour_name': tour_name})
#         return render(request, "order_form.html", {'form': form, 'tour_name': tour_name})
#
#     @staticmethod
#     def add_to_basket(request):
#         return Basket().add_to_basket(request)
