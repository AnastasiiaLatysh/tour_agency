from django.urls import path

from user.user import User

urlpatterns = [
    path(r'congrats/', User().add_info_about_user, name='congrats'),
]
