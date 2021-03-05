from django.forms import ModelForm
from .models import Profil

class usernameForm(ModelForm):
    class Meta:
        model = Profil
        fields = ('username',)
