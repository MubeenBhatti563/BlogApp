from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('post/<str:pk>', views.viewpost, name='viewpost'),
    path('newpost/', views.newpost, name='newpost'),
<<<<<<< HEAD
    path('deletepost/<str:pk>', views.deletepost, name='deletepost')
=======
    path('deletepost/<str:pk>', views.deletepost, name='deletepost'),
    path('comments/<str:pk>', views.comment, name='comment')
>>>>>>> b27d5a5 (Update project with new features)
] 