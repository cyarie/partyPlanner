from django import forms
from rsvp.models import Rsvp

class RsvpForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)
    going = forms.BooleanField(required=True)
    number_guests = forms.IntegerField(required=True)

    class Meta:
        model = Rsvp
        fields = ('name', 'going', 'number_guests',)
