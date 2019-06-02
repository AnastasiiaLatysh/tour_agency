from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'info/', views.User.add_info_about_user, name='send_tourist_info'),
]
