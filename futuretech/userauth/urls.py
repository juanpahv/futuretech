from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.signIn, name='login'),
	path('signup/', views.signUp, name='signup'),
	path('signupseller/', views.signUpAsSeller, name='signUpAsSeller'),
	path('logout/', views.signOut, name='logout'),
]

urlpatterns += [
  path('profile/', views.userProfile, name='profile'),
]

urlpatterns += [
  path('sellerprofile/', views.sellerProfile, name='sellerProfile'),
  path('sellerprofile/sellerOrders', views.sellerOrders, name='sellerOrders'),
  path('sellerprofile/sellercentral', views.sellerCentral, name='sellerCentral'),
]