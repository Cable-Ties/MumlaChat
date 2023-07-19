from django.shortcuts import render

#ログインページ
def login(request):
  login_form = forms.login_form()
  return render(request, 'login.html', context={'login_form':login_form})

#会員登録
def registration(request):
  register_form = forms.register_form()
  context_data = {'register_form': register_form}
  return render(request, 'register.html', context = context_data)