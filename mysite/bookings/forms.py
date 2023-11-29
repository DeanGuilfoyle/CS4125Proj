from django import forms

class BookingForm(forms.Form):
    days = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(1, 31)], widget=forms.Select)

class CreditCardForm(forms.Form):
    card_number = forms.CharField(label='Card Number', max_length=16)
    expiration_date = forms.DateField(label='Expiration Date')
    cvv = forms.CharField(label='CVV', max_length=4)