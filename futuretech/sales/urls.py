from django.urls import path
from . import views

urlpatterns = [
  path('profile/orders/', views.userOrders, name='userOrders'),
	path('profile/sellercentral/', views.sellerCentral, name='sellerCentral'),
	path('cart/', views.shoppingCart, name='shoppingCart'),
	path('checkout/', views.checkout, name='checkout'),
]