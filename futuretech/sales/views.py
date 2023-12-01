from django.shortcuts import render

def userOrders(request):
  return render(request, 'userOrders.html')

def sellerCentral(request):
  return render(request, 'sellerCentral.html')

def shoppingCart(request):
  return render(request, 'shoppingCart.html')

def checkout(request):
  return render(request, 'successfullOrder.html')