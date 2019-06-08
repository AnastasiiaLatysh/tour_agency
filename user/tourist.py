from django.shortcuts import render

from basket.basket import Basket
from helpers.log import log
from tours.forms import OrderTourForm
from user.user import User


class Tourist(User):

    def add_info(self, request):
        log.info("Add info about user")
        if request.method == 'POST':
            form = OrderTourForm(request.POST)
            log.info(request.POST)
            if form.is_valid():
                self.cursor.execute(f"SELECT id FROM tours WHERE nname='{form.cleaned_data.get('tour_name')}'")
                tour_id = self.cursor.fetchall()[0][0]
                self.cursor.execute(f"INSERT INTO tourists (firstname, lastname, tour_id) VALUES "
                                    f"('{form.cleaned_data.get('first_name')}', "
                                    f"'{form.cleaned_data.get('last_name')}', '{tour_id}')")
                self.cursor.execute(f"SELECT id FROM tourists WHERE firstname='{form.cleaned_data.get('first_name')}' "
                                    f"AND lastname='{form.cleaned_data.get('last_name')}'")
                tourist_id = self.cursor.fetchall()[0][0]
                self.cursor.execute(
                    f"INSERT INTO tourist_info (passport_number, foreign_passport, phone_number, tourist_id)"
                    f" VALUES ('{form.cleaned_data.get('passport_number')}', "
                    f"'{form.cleaned_data.get('foreign_passport')}','{form.cleaned_data.get('phone_number')}', "
                    f"'{tourist_id}')")
                Basket().delete_from_basket(request)
        return render(request, 'congrats.html')


tourist = Tourist()
