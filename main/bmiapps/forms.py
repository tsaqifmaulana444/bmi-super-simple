from django.forms import ModelForm
from .models import Track

class FormTrack(ModelForm):
    class Meta:
        model = Track
        fields = '__all__'