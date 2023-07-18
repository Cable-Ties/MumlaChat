from django.urls import path
from . import views

urlpatterns = [
    # path('', views.MumlaChat), #トップページ表示
    # path('MumlaChat/', views.MumlaChat), #トップページ表示
    path('login/', views.login), #ログイン
    # path('registration/', views.registration), #会員登録
    # path('logout/', views.logout), #ログアウト
]