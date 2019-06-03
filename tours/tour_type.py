from enum import Enum


class TourType(Enum):
    bus = 1
    plane = 2
    train = 3


available_tour_types = [tour_type.name for tour_type in TourType]
