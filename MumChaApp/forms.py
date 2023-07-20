from django import forms
import datetime

class login_form(forms.Form):
  loginput = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'MumlaID / Email'}), required=True)
  password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)

class register_form(forms.Form):
  user_id = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'MumlaID'}), required=True)
  email = forms.EmailField(label = '', widget = forms.EmailInput(attrs={'placeholder':'メールアドレス'}), required = True)
  password = forms.CharField(label = '', widget = forms.PasswordInput(attrs={'placeholder':'パスワード'}), required = True)
  name = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'ユーザーネーム'}), required = True)
  img = forms.ImageField(label = '', widget = forms.FileInput(attrs={'placeholder':'画像を選択'}), required = False)
  birth = forms.DateField(label = '', widget = forms.NumberInput(attrs={'type':'date'}), required = False)
  comment = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'コメント'}), required = False)

class post_form(forms.Form):
  content = forms.CharField(label='', widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'}), required=True)
  img = forms.ImageField(label = '', widget = forms.FileInput(attrs={'placeholder':'画像を選択'}), required = False)