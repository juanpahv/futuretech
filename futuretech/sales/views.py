from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from posts.models import Post, Seller
from .models import Sale, ProductSold, CartItem

@login_required
def userOrders(request):
  user = request.user
  sales = Sale.objects.filter(userId=user)
  products = ProductSold.objects.filter(saleId__in=sales)
  posts = Post.objects.filter(id__in=products)
  return render(request, 'userOrders.html', {'posts' : posts})

@login_required
def sellerCentral(request):
  if request.method == 'GET':
    user = request.user
    seller = get_object_or_404(Seller, userId=user)
    posts_count = Post.objects.filter(sellerId=seller).count()
    posts = Post.objects.filter(sellerId=seller)
    return render(request, 'sellerCentral.html', {'seller' : seller, 'user': user, 'posts_count':posts_count, 'posts': posts})

@login_required
def deletePost(request, post_id):
  seller = Seller.objects.get(userId=request.user)
  post = get_object_or_404(Post, pk=post_id, sellerId=seller)
  if request.method == 'POST':
    post.delete()
    return redirect('sellerCentral')

@login_required
def sellerOrders(request):
  user = request.user
  sales = Sale.objects.filter(userId=user)
  products = ProductSold.objects.filter(saleId__in=sales)
  posts = Post.objects.filter(id__in=products)
  return render(request, 'sellerOrders.html', {'posts' : posts})

@login_required
def shoppingCart(request):
  user = request.user
  cart_items = CartItem.objects.filter(userId=user)
  total_quantity = sum(item.quantity for item in cart_items)
  total_price = sum(item.quantity for item in cart_items)
  
  return render(request, 'shoppingCart.html', {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price})

@login_required
def checkout(request, cart_id):
  productsSold = ProductSold.objects.create(postId=cart_id)
  return render(request, 'successfullOrder.html')