from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username', widget=forms.TextInput(attrs={'class':'form'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form'}))