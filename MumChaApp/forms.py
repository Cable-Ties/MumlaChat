from django import forms
from .models import User, Post
import datetime

class login_form(forms.Form):
  loginput = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'MumlaID / Email'}), required=True)
  password = forms.CharField(label='', widget= forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)

class register_form(forms.ModelForm):
  user_id = forms.CharField(label='', widget= forms.TextInput(attrs={'placeholder':'MumlaID'}), required=True)
  email = forms.EmailField(label = '', widget = forms.EmailInput(attrs={'placeholder':'メールアドレス'}), required = True)
  password = forms.CharField(label = '', widget = forms.PasswordInput(attrs={'placeholder':'パスワード'}), required = True)
  name = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'ユーザーネーム'}), required = True)
  image = forms.ImageField(label = '', widget = forms.FileInput(attrs={'placeholder':'画像を選択'}), required = False)
  comment = forms.CharField(label = '', widget = forms.TextInput(attrs={'placeholder':'コメント'}), required = False)
  class Meta:
    model = User
    fields = ['user_id', 'email', 'password', 'name', 'image', 'comment']

class post_form(forms.ModelForm):
  content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'いまなにしてる？ｗ'}), required=True)
  image = forms.ImageField(label='', widget=forms.ClearableFileInput(), required=False)
  class Meta:
    model = Post
    fields = ['content', 'image']