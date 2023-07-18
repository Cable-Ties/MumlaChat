from django import forms
import datetime

class login_form(forms.Form):
  user_id = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'MumlaID'}), required=True)
  password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)

