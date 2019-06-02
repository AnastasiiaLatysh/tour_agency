from django.db import connection
from django.shortcuts import render

cursor = connection.cursor()


class Basket(object):

    @staticmethod
    def open_basket(request):
        print("Open basket")
        cursor.execute("SELECT tour_id from basket")
        if cursor.fetchall():
            cursor.execute("SELECT nname, price FROM tours WHERE id in (SELECT tour_id from basket)")
            ordered_tours = []
            for row in cursor.fetchall():
                ordered_tours.append(row)
            context = {'ordered_tours': ordered_tours}
            return render(request, "basket.html", context)
        else:
            return render(request, "empty_basket.html")

    def add_to_basket(self, request):
        print("Add basket")
        chosen_tours = request.POST.getlist('chosen')
        for tour_name in chosen_tours:
            cursor.execute(f"SELECT id FROM tours WHERE nname='{tour_name}'")
            tour_id = cursor.fetchall()[0][0]
            cursor.execute(f"INSERT INTO basket (tour_id) VALUES ('{tour_id}')")
        return self.open_basket(request)

    @staticmethod
    def delete_from_basket(request):
        cursor.execute(f"SELECT id FROM tours WHERE nname='{request.POST.get('tour_name')}'")
        tour_id = cursor.fetchall()[0][0]
        cursor.execute(f"DELETE FROM basket WHERE tour_id='{tour_id}'")
        return Basket.open_basket(request)
