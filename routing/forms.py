from django import forms


class NameForm(forms.Form):
    number_1 = forms.IntegerField(label='Input your number_1')
    number_2 = forms.IntegerField(label='Input your number_2')
