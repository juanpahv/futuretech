from django.urls import path
from . import views

urlpatterns = [
  path('', views.listPosts, name='home'),
]

urlpatterns += [
  path('product/<int:post_id>/', views.productPage, name='productPage'), 
]

urlpatterns += [
	path('profile/sellercentral/createpost/', views.createPost, name='createPost'),
  path('profile/sellercentral/modifypost/<int:post_id>/', views.modifyPost, name='modifyPost'),
]

