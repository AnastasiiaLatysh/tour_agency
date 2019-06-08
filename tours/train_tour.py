from django.db import models

from tours.tour import Tour


class TrainTour(Tour):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_id = models.PositiveSmallIntegerField(default=3)
        self._second_class_sleeper = models.BooleanField(default=False)
        self._first_class_sleeper = models.BooleanField(default=True)

    def __str__(self):
        return super().__str__() + f", tour type - {self.id}"

    def cursor_with_all_tours(self):
        self.cursor.execute(self.all_tours + "AND type_id={}".format(self.type_id.default))
        return self.cursor

    def print_full_info(self):
        seats_type = 'first' if self.first_class_sleeper else 'second'
        print(self.__str__() + f", {seats_type} class sleeper seats.")

    @property
    def second_class_sleeper(self):
        return self.second_class_sleeper

    @second_class_sleeper.setter
    def second_class_sleeper(self, is_second_class_sleeper):
        self._second_class_sleeper = is_second_class_sleeper

    @property
    def first_class_sleeper(self):
        return self._first_class_sleeper

    @first_class_sleeper.setter
    def first_class_sleeper(self, is_first_class_sleeper):
        self._first_class_sleeper = is_first_class_sleeper


train_tour = TrainTour()
