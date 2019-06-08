from django.db import models, connection
from django.shortcuts import render

from helpers.log import log
from tours.forms import TourForm


class Tour(object):

    all_tours = "SELECT nname, price, available_seats FROM tours WHERE available_seats > 0 "

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cursor = connection.cursor()
        self.id = models.BigIntegerField(primary_key=True)
        self.name = models.CharField(max_length=50)
        self.price = models.DecimalField(max_digits=5, decimal_places=2)
        self.type_id = models.PositiveSmallIntegerField()
        self.available_seats = models.IntegerField()
        self.county_id = models.PositiveSmallIntegerField()
        self.city_id = models.PositiveIntegerField()
        self.type_id = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Tour '{self.name}': price - {self.price}, country - {self.county_id}," \
            f" city - {self.city_id}, available_seats - {self.available_seats}"

    def cursor_with_all_tours(self):
        log.info("Getting all tours from data base")
        log.info(self.all_tours)
        self.cursor.execute(self.all_tours)
        return self.cursor

    def show_all_tours(self, request, auth=False):
        log.info(f"Showing tours for user with status {auth}")
        tours = []
        for row in self.cursor_with_all_tours().fetchall():
            tours.append(row)
        context = {'tours': tours}
        return render(request, "all_tours.html", context) if not auth \
            else render(request, "auth_all_tours.html", context)

    def edit(self, request, auth=False):
        tours = []
        for row in self.cursor_with_all_tours().fetchall():
            tours.append(row)
        form = TourForm()
        return render(request, "edit.html", {'form': form, 'tours': tours}) if auth else self.show_all_tours(request,
                                                                                                             auth=False)


tour = Tour()
