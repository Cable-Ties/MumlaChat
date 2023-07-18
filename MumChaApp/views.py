from django.shortcuts import render

#ログインページ
def login(request):
  login_form = forms.login_form()
  return render(request, 'login.html', context={'login_form':login_form})