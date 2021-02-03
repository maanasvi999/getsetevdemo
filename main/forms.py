from django import forms
from .models import Subscribers

class EmailForm(forms.Form):
    email = forms.EmailField(required=True, label = "Enter Email", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Subscribers
        fields = ["email", "subscribed_time"]