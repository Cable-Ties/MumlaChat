from django import forms
import datetime

class login_form(forms.Form):
  loginput = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'MumlaID / Email'}), required=True)
  password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)

class register_form(forms.Form):
  user_id = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'MumlaID'}), required=True)
  email = forms.CharField(label = '', widget = forms.EmailInput(attrs={'placeholder':'メールアドレス'}), required = True)
  password = forms.CharField(label = '', widget = forms.PasswordInput(attrs={'placeholder':'パスワード'}), required = True)
  name = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'ユーザーネーム'}), required = True)
  img = forms.ImageField(label = '', widget = forms.FileInput(attrs={'placeholder':'画像を選択'}))
  birth = forms.DateField(label = '', widget = forms.NumberInput(attrs={'placeholder':'誕生日'}))
  comment = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'コメント'}))