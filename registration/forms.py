from django.forms import ModelForm
from registration.models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['first_name','last_name','email','phone_number',
            'gender','skill','wants_shirt','wants_frisbee','shirt_size','position']
