from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.hi, name='home'),
   path('contact', views.contact, name='contact'),
   path('portfolio', views.portfolio, name='portfolio'),
   path('register', views.registerPage, name='register'),
   path('login', views.loginpage, name='login'),
   path('logout', views.logoutUser, name='logout'),
   path('account', views.accountPage, name='account'),
   path('editprofile', views.UserEditView, name='editprofile'),
]