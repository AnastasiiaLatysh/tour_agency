from django.db import models

from tours.tour import Tour


class BusTour(Tour):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_id = models.PositiveSmallIntegerField(default=1)
        self.two_floored_bus = models.BooleanField(default=False)

    def __str__(self):
        return super().__str__() + f", two floored bus - {self.two_floored_bus}"

    def cursor_with_all_tours(self):
        self.cursor.execute(self.all_tours + " AND type_id={}".format(self.type_id.default))
        return self.cursor

    @property
    def two_floored_bus(self):
        return self._two_floored_bus

    @two_floored_bus.setter
    def two_floored_bus(self, is_two_floored_bus):
        self._two_floored_bus = is_two_floored_bus


bus_tour = BusTour()
