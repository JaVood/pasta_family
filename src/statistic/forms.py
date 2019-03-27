from django import forms
from .models import DayliStatistic


class DayliStatisticForm(forms.ModelForm):
    class Meta:
        model = DayliStatistic
        fields = '__all__'


