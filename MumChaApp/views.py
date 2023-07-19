from django.shortcuts import render
from django.db.models import Q
from . import forms
from . import models
import datetime

#ログインページ
def firstlogin(request):
  login_form = forms.login_form()
  return render(request, 'login.html', context={'login_form':login_form})

def login(request):
  login_form = forms.login_form(request.POST)
  if login_form.is_valid():
    try:
      # loginput が MumlaIDとemailのいずれかと一致するか
      login_user = models.User.objects.get(Q(password = login_form.cleaned_data['password']), Q(user_id = login_form.cleaned_data['loginput'])|Q(email = login_form.cleaned_data['loginput']))
      if login_form.cleaned_data['loginput'] == login_user.user_id and login_form.cleaned_data['password'] == login_user.password:
        return render(request, 'MumlaChat.html')
      if login_form.cleaned_data['loginput'] == login_user.email and login_form.cleaned_data['password'] == login_user.password:
        return render(request, 'MumlaChat.html')
      # loginput が MumlaIDとemail のいずれでもない場合
      return firstlogin(request)
    except(models.User.DoesNotExist):
      print("特定の値がないらしい")
      return firstlogin(request)

#会員登録フォーム
def register(request):
  register_form = forms.register_form()
  context_data = {'register_form': register_form}
  return render(request, 'register.html', context = context_data)

#会員登録完了
def registration(request):
  register_form = forms.register_form(request.POST)
  if register_form.is_valid():
    request.session['user_id'] = register_form.cleaned_data['user_id']
    request.session['email'] = register_form.cleaned_data['email']
    request.session['password'] = register_form.cleaned_data['password']
    request.session['name'] = register_form.cleaned_data['name']
    request.session['img'] = register_form.cleaned_data['img']
    request.session['birth'] = register_form.cleaned_data['birth']
    request.session['comment'] = register_form.cleaned_data['comment']
    print(request.session['email'])
    models.User.objects.create(
      user_id = request.session['user_id'],
      email = request.session['email'],
      password = request.session['password'],
      name = request.session['name'],
      img = request.session['img'],
      birth = request.session['birth'],
      comment = request.session['comment'],
    )
  return firstlogin(request)