from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def userOrders(request):
  return render(request, 'userOrders.html')

def sellerCentral(request):
  return render(request, 'sellerCentral.html')

@login_required
def shoppingCart(request):
  return render(request, 'shoppingCart.html')

def checkout(request):
  return render(request, 'successfullOrder.html')