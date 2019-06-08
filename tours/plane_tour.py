from django.db import models
from tours.tour import Tour


class PlaneTour(Tour):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_id = models.PositiveSmallIntegerField(default=2)
        self._is_hand_luggage = models.BooleanField(default=True)

    def __str__(self):
        return super().__str__() + f", tour type - {self.type_id}"

    def cursor_with_all_tours(self):
        self.cursor.execute(self.all_tours + "AND type_id={}".format(self.type_id.default))
        return self.cursor

    @property
    def hand_luggage(self):
        return self._is_hand_luggage

    @hand_luggage.setter
    def hand_luggage(self, is_hand_luggage):
        self._is_hand_luggage = is_hand_luggage


plane_tour = PlaneTour()
