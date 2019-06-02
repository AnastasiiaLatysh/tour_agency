from django.db import connection

# Create your views here.
# from tours.models import Tours


from basket.views import Basket
from tours.forms import OrderTourForm
from tours.views import Tours

cursor = connection.cursor()


class User(object):

    @staticmethod
    def add_info_about_user(request):

        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = OrderTourForm(request.POST)
            print(request.POST)
            # check whether it's valid:
            if form.is_valid():
                cursor.execute(f"INSERT INTO tourists (firstname, lastname) VALUES "
                               f"('{form.cleaned_data.get('first_name')}', '{form.cleaned_data.get('last_name')}')")
                cursor.execute(f"SELECT  id FROM tourists WHERE firstname='{form.cleaned_data.get('first_name')}' AND "
                               f"lastname='{form.cleaned_data.get('last_name')}'")
                tourist_id = cursor.fetchall()[0][0]
                cursor.execute(f"INSERT INTO tourist_info (passport_number, foreign_passport, phone_number, tourist_id)"
                               f" VALUES ('{form.cleaned_data.get('passport_number')}', "
                               f"'{form.cleaned_data.get('foreign_passport')}',"
                               f"'{form.cleaned_data.get('phone_number')}', '{tourist_id}')")
                Basket.delete_from_basket(request)
        return Tours.show_all_tours(request)
