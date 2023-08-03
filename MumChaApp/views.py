from django.shortcuts import render, get_object_or_404
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
        request.session['user_id'] = login_user.user_id
        return render(request, 'MumlaChat.html')
      if login_form.cleaned_data['loginput'] == login_user.email and login_form.cleaned_data['password'] == login_user.password:
        request.session['user_id'] = login_user.user_id
        return render(request, 'MumlaChat.html')
      # loginput が MumlaIDとemail のいずれでもない場合
      return firstlogin(request)
    except(models.User.DoesNotExist):
      print("特定の値がないらしい")
      return firstlogin(request)

#ログアウト
def logout(request):
  request.session.flush()
  return firstlogin(request)

#会員登録フォーム
def register(request):
  params = {
    'register_form': forms.register_form(),
  }
  return render(request, 'register.html', params)

#会員登録完了
def registration(request):
  if (request.method == 'POST'):
    nowtime = datetime.datetime.now()
    request.FILES["image"].name = str(nowtime) + '.png'
    form = forms.register_form(request.POST, request.FILES)
    if form.is_valid():
      form.save()
  return firstlogin(request)

#投稿ホーム
def home(request):
  tweet_list = models.Post.objects.all()
  tweet_list = list(tweet_list)
  tweet_list.reverse()
  params = {
    'tweet_list':tweet_list
    }
  return render(request, 'home.html', params)

#投稿入力
def tweet(request):
  params = {
    'post_form': forms.post_form()
    }
  return render(request, 'tweet.html', params)

#投稿完了
def tweeting(request):
  if (request.method == 'POST'):
    post_form = forms.post_form(request.POST, request.FILES)
    if post_form.is_valid():
      if post_form.cleaned_data['image'] is not None:
        nowtime = datetime.datetime.now()
        request.FILES["image"].name = str(nowtime) + '.png'
        post_form = forms.post_form(request.POST, request.FILES)
        if post_form.is_valid():
          models.Post.objects.create(
            content = post_form.cleaned_data['content'],
            owner = models.User.objects.get(user_id=request.session['user_id']),
            image = post_form.cleaned_data['image'],
            post_date = datetime.datetime.now(),
          )
      else:
        models.Post.objects.create(
          content = post_form.cleaned_data['content'],
          owner = models.User.objects.get(user_id=request.session['user_id']),
          post_date = datetime.datetime.now(),
        )
  return home(request)
