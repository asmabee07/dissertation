from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import CompleteProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=40, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=40, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', )


GENDER_SELECTION = [
    ('F', 'Female'),
    ('M', 'Male')
]

ACTIVITY_FACTOR = [
    ('1.2', 'Sedentary'), ('1.55', 'Moderately Active'), ('1.725', 'Active')
]


class CompleteProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_SELECTION)
    activity_factor = forms.ChoiceField(widget=forms.RadioSelect, choices=ACTIVITY_FACTOR)

    class Meta:
        model = CompleteProfile
        fields = ["gender", "age", "weight", "height", "activity_factor"]

    ''' 
    def save(self, commit=True):
        instance = super(CompleteProfileForm, self).save(commit=False)
        instance.height = float(instance.height)/3.68
        if commit:
            instance.save()
        return instance
'''


'''
class BmiMeasurementForm(forms.ModelForm):
    class Meta:
        model = BmiMeasurement
        fields = ["id", "weight_in_kg", "height_in_meters", "measured_at"]
'''
