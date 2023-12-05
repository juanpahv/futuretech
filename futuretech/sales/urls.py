from django.urls import path
from . import views

urlpatterns = [
  path('profile/orders/', views.userOrders, name='userOrders'),
	path('cart/', views.shoppingCart, name='shoppingCart'),
	path('checkout/', views.checkout, name='checkout'),
  path('sellerprofile/sellerorders', views.sellerOrders, name='sellerOrders'),
]

urlpatterns += [
  path('sellerprofile/sellercentral/', views.sellerCentral, name='sellerCentral'),
  path('sellerprofile/sellercentral/<int:post_id>/delete/', views.deletePost, name='deletePost'),
]