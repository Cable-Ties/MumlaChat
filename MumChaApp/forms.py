from django import forms
import datetime

class login_form(forms.Form):
  email = forms.EmailField(label='', widget= forms.EmailInput(attrs={'placeholder':'email'}), required=True)
  password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)

