
from django.forms import ModelForm
from wedding.models import People


# Let us use ye olde ModelForm to automagically generate a form
class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ['name', 'address1', 'address2', 'city', 'state', 'zip_code', 'email', 'comment']