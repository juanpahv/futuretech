from email.mime import image
from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm, PostImageForm, QuantityForm
from .models import Post, Seller, Category
from sales.models import ProductSold, Sale

def navBar(request):
  user = request.user
  is_seller = Seller.objects.filter(userId=user).exists()
  return render(request, 'navbar.html', {'user': user}, {'seller': is_seller})

def listPosts(request):
  phones = Category.objects.get(name='Phones')
  headphones = Category.objects.get(name='Headphones')
  laptops = Category.objects.get(name='Laptops')
  gameConsoles = Category.objects.get(name='Game Consoles')
  peripherals = Category.objects.get(name='Peripherals')

  PhonesPosts = Post.objects.filter(categoryId=phones)
  HeadphonesPosts = Post.objects.filter(categoryId=headphones)
  LaptopsPosts = Post.objects.filter(categoryId=laptops)
  GameConsolesPosts = Post.objects.filter(categoryId=gameConsoles)
  PeripheralsPosts = Post.objects.filter(categoryId=peripherals)
  
  AllPosts = Post.objects.all()
  context = {
    'posts': AllPosts,
    'phones': PhonesPosts,
    'headphones': HeadphonesPosts,
    'laptops': LaptopsPosts,
    'gameConsoles': GameConsolesPosts,
    'peripherals': PeripheralsPosts,
  }
  return render(request, 'index.html', context)

def productPage(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  form = QuantityForm()
  return render(request, 'productPage.html', {'post': post, 'form': form})
  
@login_required
def modifyPost(request, post_id):
  if request.method == 'GET':
    try:
      seller = Seller.objects.get(userId=request.user)
      post = get_object_or_404(Post, pk=post_id, sellerId=seller)
      form = PostForm(instance=post)
    except ValueError:
      return redirect('sellerCentral')
    return render(request, 'modifyPost.html', {'post': post, 'form': form})
  else:
    try:
      seller = Seller.objects.get(userId=request.user)
      post = get_object_or_404(Post, pk=post_id, sellerId=seller)
      form = PostForm(instance=post)
      form.save()
      return redirect('sellerCentral')
    except ValueError:
      return render(request, 'modifyPost.html', {'post': post, 'form': form, 'error': 'Bad data passed in. Try again.'})

@login_required
def createPost(request):
    if request.method == 'GET':
        return render(request, 'createPost.html', {'form': PostForm, 'imageForm': PostImageForm})
    else:
        imageForm = PostImageForm(request.POST, request.FILES)
        form = PostForm(request.POST)
        if form.is_valid():
            seller = Seller.objects.get(userId=request.user)
            new_post = form.save(commit=False)
            new_post.sellerId = seller
            new_post.save()
            image = imageForm.save(commit=False)
            image.postId = new_post
            image.save()
            return redirect('sellerCentral')
        else:
            return render(request, 'createPost.html', {'form': form, 'imageForm': imageForm, 'error': 'Bad data passed in. Try again.'})
        
@login_required
def buyNow(request, post_id):
  if request.method == 'GET':
    post = get_object_or_404(Post, pk=post_id)
    form = QuantityForm()
    return render(request, 'productPage.html', {'post': post, 'form': form})
  else:
    form = QuantityForm(request.POST)
    post = get_object_or_404(Post, pk=post_id)
    if form.is_valid():
      quantity = form.cleaned_data['quantity']
      sale = Sale.objects.create(userId=request.user)
      ProductSold.objects.create(postId=post, saleId=sale, pricePerunit=post.originalPrice, amount=quantity)
      post.stock -= quantity
      return redirect('home')
    else:
      return render(request, 'productPage.html', {'post': post, 'form': form, 'error': 'Bad data passed in. Try again.'})