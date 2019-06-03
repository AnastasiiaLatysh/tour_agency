from django.db import connection
from django.shortcuts import render

from basket.basket import Basket
from tours.forms import OrderTourForm


class User(object):
    def __init__(self):
        self.cursor = connection.cursor()
    #
    # def __str__(self):
    #     return f"User info: first name {self.first_name}, last name - {self.last_name}"

    def add_info_about_user(self, request):
        if request.method == 'POST':
            form = OrderTourForm(request.POST)
            if form.is_valid():
                self.cursor.execute(f"INSERT INTO tourists (firstname, lastname) VALUES "
                                    f"('{form.cleaned_data.get('first_name')}', '{form.cleaned_data.get('last_name')}')")
                self.cursor.execute(f"SELECT  id FROM tourists WHERE firstname='{form.cleaned_data.get('first_name')}' "
                                    f"AND lastname='{form.cleaned_data.get('last_name')}'")
                tourist_id = self.cursor.fetchall()[0][0]
                self.cursor.execute(f"INSERT INTO tourist_info (passport_number, foreign_passport, phone_number, tourist_id)"
                               f" VALUES ('{form.cleaned_data.get('passport_number')}', "
                               f"'{form.cleaned_data.get('foreign_passport')}',"
                               f"'{form.cleaned_data.get('phone_number')}', '{tourist_id}')")
                Basket().delete_from_basket(request)
        return render(request, 'congrats.html')
