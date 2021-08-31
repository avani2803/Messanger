from django.urls import path

from . import views

urlpatterns = [
    #Index Page
    path('',views.home,name='home'),
      #User Register
    path('register',views.register,name='register'),

    # User Register
    path('login',views.login,name='login'),

    #logout
    path('logout',views.Logout, name='logout'),

    path('message',views.message, name='message'),

]
