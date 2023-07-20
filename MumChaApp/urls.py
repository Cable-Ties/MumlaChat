from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstlogin), #トップページ表示
    path('MumlaChat/', views.MumlaChat), #トップページ表示
    path('login/', views.login), #ログイン
    path('register/', views.register), #会員登録フォーム
    path('registration/', views.registration), #会員登録
    path('logout/', views.logout), #ログアウト
    path('home/', views.home),
    # path('logout/', views.logout), #ログアウト
    # path('tweet/', views.tweet), #投稿
]