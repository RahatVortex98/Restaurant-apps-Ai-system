from django import forms
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete':'off', 'placeholder': 'Enter your password'})
    )
    show = forms.BooleanField(
        label="Show Password",
        widget=forms.CheckboxInput(attrs={'id': 'show-password-checkbox'}),
        required=False
    )
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # If both username and password are provided, authenticate the user
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password.")

        return cleaned_data