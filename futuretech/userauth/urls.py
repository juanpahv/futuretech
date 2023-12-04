from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.signIn, name='login'),
	path('signup/', views.signUp, name='signup'),
	path('signupseller/', views.signUpAsSeller, name='signUpAsSeller'),
	path('logout/', views.signOut, name='logout'),
  path('profile/', views.userProfile, name='profile'),
]