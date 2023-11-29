from django import forms
from .models import Car

#form to be displayed on list page and filter page
class CarFilterForm(forms.Form):
    car_make = forms.ChoiceField(
        choices=[('', 'All Car Types')] + list(Car.objects.values_list('make', 'make').distinct()),
        required=False
    )
    car_year = forms.ChoiceField(
        choices=[('', 'All Car Years')] + list(Car.objects.values_list('year', 'year').distinct()),
        required=False
    )
    car_colour = forms.ChoiceField(
        choices=[('', 'All Car Colors')] + list(Car.objects.values_list('colour', 'colour').distinct()),
        required=False
    )
    max_price = forms.DecimalField(min_value=0, required=False)
    #start_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=range(2023, 2030)))
    #end_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=range(2023, 2030)))