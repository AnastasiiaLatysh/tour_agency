from django.db import models, connection
from django.shortcuts import render


class Tour(object):

    all_tours = "SELECT nname, price, available_seats FROM tours WHERE available_seats > 0 "

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cursor = connection.cursor()
        self.id = models.BigIntegerField(primary_key=True)
        self.name = models.CharField(max_length=50)
        self.price = models.DecimalField(max_digits=5, decimal_places=2)
        self.county_id = models.PositiveSmallIntegerField()
        self.city_id = models.PositiveIntegerField()
        self.type_id = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Tour '{self.name}': price - {self.price}, country - {self.county_id}," \
            f" city - {self.city_id}"

    def cursor_with_all_tours(self):
        self.cursor.execute(self.all_tours)
        return self.cursor

    def show_all_tours(self, request):
        tours = []
        for row in self.cursor_with_all_tours().fetchall():
            tours.append(row)
        context = {'tours': tours}
        return render(request, "all_tours.html", context)

    # def add_vehicle_model(self):
    #     print("Enter vehicle model:\n")
    #     self.vehicle_model = input()
    #
    # def update_price(self):
    #     print("Enter new price:\n")
    #     self.price = input()
