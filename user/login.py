from django.db import connection
from django.shortcuts import render

from helpers.log import log
from tours.forms import LoginForm
from tours.tour import Tour


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class UserAuth(object, metaclass=Singleton):

    def __init__(self):
        self.cursor = connection.cursor()

    def login(self, request):
        if request.method == 'GET':
            form = LoginForm()
            return render(request, "login_page.html",  {'form': form})
        elif request.method == 'POST':
            return self.authorization(request)

    def authorization(self, request):
        form = LoginForm(request.POST)
        log.info(request.POST)
        if form.is_valid():
            self.cursor.execute(f"SELECT id FROM tour_agent WHERE nname='{form.cleaned_data.get('name')}' AND "
                                f"ppassword='{form.cleaned_data.get('password')}'")
            user = self.cursor.fetchall()
            if user:
                self.cursor.execute(f"UPDATE tour_agent SET auth=True WHERE nname='{form.cleaned_data.get('name')}'")
                return Tour().show_all_tours(request, auth=True)
            else:
                return render(request, 'not_auth.html', status=403)

    def logout(self, request):
        self.cursor.execute(f"UPDATE tour_agent SET auth=False WHERE nname='admin'")
        return Tour().show_all_tours(request, auth=False)


user_login = UserAuth()
