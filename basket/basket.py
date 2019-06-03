from django.db import connection
from django.shortcuts import render

from tours.forms import OrderTourForm


class Basket(object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cursor = connection.cursor()

    def open_basket(self, request):
        print("Open basket")
        self.cursor.execute("SELECT tour_id from basket")
        if self.cursor.fetchall():
            self.cursor.execute("SELECT nname, price FROM tours WHERE id in (SELECT tour_id from basket)")
            ordered_tours = []
            for row in self.cursor.fetchall():
                ordered_tours.append(row)
            context = {'ordered_tours': ordered_tours}
            return render(request, "basket.html", context)
        else:
            return render(request, "empty_basket.html")

    def add_to_basket(self, request):
        print("Add basket")
        chosen_tours = request.POST.getlist('chosen')
        for tour_name in chosen_tours:
            self.cursor.execute(f"SELECT id FROM tours WHERE nname='{tour_name}'")
            tour_id = self.cursor.fetchall()[0][0]
            self.cursor.execute(f"INSERT INTO basket (tour_id) VALUES ('{tour_id}')")
        return self.open_basket(request)

    def delete_from_basket(self, request):
        self.cursor.execute(f"SELECT id FROM tours WHERE nname='{request.POST.get('tour_name')}'")
        tour_id = self.cursor.fetchall()[0][0]
        self.cursor.execute(f"DELETE FROM basket WHERE tour_id='{tour_id}'")
        return self.open_basket(request)

    @staticmethod
    def order_tour(request):
        tour_name = request.GET.get('tour_name')
        form = OrderTourForm(initial={'tour_name': tour_name})
        return render(request, "order_form.html", {'form': form, 'tour_name': tour_name})
