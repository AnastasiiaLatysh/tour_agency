from django.urls import path

from user.tour_agent import tour_agent
from user.tourist import tourist
from user.user import user

urlpatterns = [
    path(r'congrats/', tourist.add_info, name='congrats'),
    path(r'admin/', user.login, name='login'),
    path(r'admin/update/', tour_agent.update_tours_info, name='update_tours_info'),
    path(r'admin/edit/', tour_agent.edit_tour, name='edit_tour'),
    path(r'logout/', tour_agent.logout, name='logout'),
]
