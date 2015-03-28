
from django import forms
from wedding.models import People


# Let us use ye olde forms to automagically generate a form
class PeopleForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)
    address1 = forms.CharField(max_length=255, required=True)
    address2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=255, required=True)
    state = forms.CharField(max_length=2, required=True)
    zip_code = forms.IntegerField(required=True)
    email = forms.CharField(max_length=255, required=False)
    comment = forms.Textarea()

    class Meta:
        model = People
        fields = ('name', 'address1', 'address2', 'city', 'state', 'zip_code', 'email', 'comment',)