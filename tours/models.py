from django.db import models


# Create your models here.


class Tours(models.Model):
    id = models.BigIntegerField(primary_key=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    county_id = models.PositiveSmallIntegerField()
    city_id = models.PositiveIntegerField()
    type_id = models.PositiveSmallIntegerField()
    vehicle_type = models.PositiveSmallIntegerField()
    duration_id = models.PositiveSmallIntegerField()
    available_seats = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "tours"
