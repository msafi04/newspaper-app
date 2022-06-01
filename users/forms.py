#users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        #field = UserCreationForm.Meta.fields + ('age', )
        fields = ('username', 'email', 'age')
    
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        #field = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age')