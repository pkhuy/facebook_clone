from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    path('message', views.message, name='message'),
    path('newfeed', views.newfeed , name='newfeed'),
    path('like', views.like , name='likepost'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('<str:room>/', views.getMessages, name='getMessages'),
]
