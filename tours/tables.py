import django_tables2 as tables


class AllTours(tables.Table):

    name = tables.Column(attrs={'td': {'class': 'account'}})
    price = tables.Column(attrs={'td': {'class': 'account'}})
    available_seats = tables.Column(attrs={'td': {'class': 'account'}})

