from django import forms
from .models import Profile, Match
from django.utils import timezone

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateTimeInput):
    input_type = 'time'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('teamname','introduce','city','home', 'member','made_on','profile_photo',)
        widgets = {
            'made_on': DateInput(),
            'book': TimeInput(),
        }

class MatchForm(forms.ModelForm):
    book = forms.DateField(required=False)
    class Meta:
        model = Match
        fields =('home','member','made_on','book')
        widgets = {
            'made_on': DateInput(),
            'book': TimeInput(),
        }