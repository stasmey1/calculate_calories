from django.forms import *
from .models import *


class ProfileAddForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'photo', 'height', 'weight', 'age', 'sex', 'target', 'activity',)
