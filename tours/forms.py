from django import forms


class OrderTourForm(forms.Form):

    tour_name = forms.CharField(label='Tour name', max_length=50, widget=forms.HiddenInput(), required=True)
    first_name = forms.CharField(label='First name', max_length=30, required=True)
    last_name = forms.CharField(label='Last name', max_length=30, required=True)
    passport_number = forms.CharField(label='Passport number', max_length=15, required=False)
    foreign_passport = forms.CharField(label='Foreign passport', max_length=15, required=False)
    phone_number = forms.CharField(label='Phone number', max_length=15, required=True)


class LoginForm(forms.Form):

    name = forms.CharField(label='User name', max_length=50, required=True)
    password = forms.CharField(label='User password', max_length=20, required=True)


class TourForm(forms.Form):

    name = forms.CharField(label='Name', max_length=50, required=False)
    price = forms.CharField(label='Price', max_length=50, required=False)
    available_seats = forms.CharField(label='Available seats', max_length=3, required=False)
