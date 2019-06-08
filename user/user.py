from django.db import connection

from tours.tour import Tour
from user.login import UserAuth


class User(object):

    def __init__(self):
        self.cursor = connection.cursor()
        self.user_login = UserAuth()

    def is_authorized(self):
        self.cursor.execute(f"SELECT auth FROM tour_agent")
        return bool(self.cursor.fetchall()[0][0])

    def login(self, request):
        if self.is_authorized():
            return Tour().show_all_tours(request, auth=True)
        else:
            return self.user_login.login(request)

    def logout(self, request):
        self.user_login.logout(request)
        return Tour().show_all_tours(request, auth=False)


user = User()
