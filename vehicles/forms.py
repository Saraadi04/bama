from django import forms

class PurchaseForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    contact_info = forms.CharField(lable='Information', max_length=100)
    payment_method = forms.ChoiceField(choices=[('credit', 'Credit Card'), ('debit', 'Debit Card'), ('paypal', 'Paypal')])
    city = forms.CharField(label='City', max_length='100')