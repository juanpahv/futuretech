"""
URL configuration for futuretech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from userauth import views as userauth_views
from posts import views as posts_views
from sales import views as sales_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', userauth_views.signIn, name='login'),
    path('signup/', userauth_views.signUp, name='signup'),
    path('signupseller/', userauth_views.signUpAsSeller, name='signUpAsSeller'),
    path('logout/', userauth_views.signOut, name='logout'),
    path('', posts_views.home, name='home'),
    path('profile/', userauth_views.userProfile, name='profile'),
    path('profile/orders/', sales_views.userOrders, name='userOrders'),
    path('profile/sellercentral/', sales_views.sellerCentral, name='sellerCentral'),
    path('profile/sellercentral/modifypost/', posts_views.modifyPost, name='modifyPost'),
    path('product/', posts_views.productPage, name='productPage'),
    path('cart/', sales_views.shoppingCart, name='shoppingCart'),
    path('checkout/', sales_views.checkout, name='checkout'),
]
