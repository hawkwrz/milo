from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'birthday', 'password1', 'password2',)
        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'datepicker'}, format='%d/%m/%Y'),
        }
