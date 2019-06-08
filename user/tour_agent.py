from django.shortcuts import render

from helpers.log import log
from tours.forms import TourForm
from tours.tour import Tour
from user.user import User


class TourAgent(User):

    def update_tours_info(self, request):
        log.info("Add info about user")
        if request.method == 'POST':
            form = TourForm(request.POST)
            log.info(request.POST)
            if form.is_valid():
                log.info(f"UPDATE tours SET price={form.cleaned_data.get('price')},"
                                    f"available_seats={form.cleaned_data.get('available_seats')} "
                                    f"WHERE nname='{form.cleaned_data.get('name')}'")
                self.cursor.execute(f"UPDATE tours SET price={form.cleaned_data.get('price')},"
                                    f"available_seats={form.cleaned_data.get('available_seats')} "
                                    f"WHERE nname='{form.cleaned_data.get('name')}'")
        return render(request, 'tour_updated.html')

    def edit_tour(self, request):
        return Tour().edit(request, self.is_authorized())


tour_agent = TourAgent()
