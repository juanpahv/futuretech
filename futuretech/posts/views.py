from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm, PostImageForm
from .models import Post, Seller

def postsInCart(post):
  posts = []
  
  return posts

def navBar(request):
  user = request.user
  is_seller = Seller.objects.filter(userId=user).exists()
  return render(request, 'navbar.html', {'user': user}, {'seller': is_seller})

def listPosts(request):
  posts = Post.objects.all()
  return render(request, 'index.html', {'posts': posts})

def productPage(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  return render(request, 'productPage.html', {'post': post})

@login_required
def modifyPost(request, post_id):
  if request.method == 'GET':
    try:
      sellerId = Seller.objects.get(userId=request.user)
      post = get_object_or_404(Post, pk=post_id, sellerId=sellerId)
      form = PostForm(instance=post)
    except ValueError:
      return redirect('sellerCentral')
    return render(request, 'modifyPost.html', {'post': post, 'form': form})
  else:
    try:
      sellerId = Seller.objects.get(userId=request.user)
      post = get_object_or_404(Post, pk=post_id, sellerId=sellerId)
      form = PostForm(request.POST, instance=post)
      form.save()
      return redirect('sellerCentral')
    except ValueError:
      return render(request, 'modifyPost.html', {'post': post, 'form': form, 'error': 'Bad data passed in. Try again.'})


@login_required
def createPost(request):
  if request.method == 'GET':
    image = PostImageForm()
    return render(request, 'createPost.html', {'form': PostForm, 'image': image})
  else:
      form = PostForm(request.POST)
      image = PostImageForm(request.POST, request.FILES)

      newPost = form.save(commit=False)
      seller = Seller.objects.get(userId=request.user)
      newPost.sellerId = seller
      newPost.save()

      image_instance = image.save(commit=False)
      image_instance.postId = newPost
      image_instance.save()
      return redirect('sellerCentral')