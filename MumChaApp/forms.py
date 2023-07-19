from django import forms
import datetime

class login_form(forms.Form):
  email = forms.EmailField(label='', widget= forms.EmailInput(attrs={'placeholder':'email'}), required=True)
  password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)

class register_form(form.Form):
  email = forms.CharField(label = '', widget = forms.EmailInput(attrs={'placeholder':'メールアドレス'}), required = True)
  password = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'パスワード'}), required = True)
  name = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'ユーザーネーム'}), required = True)
  img = forms.ImageField(label = '', widget = forms.ImageInput(attrs={'placeholder':'画像を選択'}))
  birth = forms.DateField(label = '', widget = forms.DateInput(attrs={'placeholder':'誕生日'}))
  comment = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'コメント'}))