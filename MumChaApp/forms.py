from django import forms
import datetime

class login_form(forms.Form):
  loginput = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'MumlaID / Email'}), required=True)
  password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)

