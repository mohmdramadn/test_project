from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput())
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.PasswordInput()
    balance = forms.IntegerField()
    type = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'balance', 'type')

    # def save(self, commit=True):
    #     user = super(SignupForm, self).save(commit=False)
    #     user.username = self.cleaned_data['username']
    #     user.email = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.password = self.cleaned_data['password']
    #     user.balance = self.cleaned_data['balance']
    #     user.type = self.cleaned_data['type']
    #
    #     if commit:
    #         user.save()
    #     return user
