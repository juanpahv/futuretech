from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Seller

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
    return render(request, 'createPost.html', {'form': PostForm})
  else:
    try:
      form = PostForm(request.POST)
      newPost = form.save(commit=False)
      seller = Seller.objects.get(userId=request.user)
      newPost.sellerId = seller
      newPost.save()
      return redirect('sellerCentral')
    except ValueError:
      return render(request, 'createPost.html', {'form': PostForm, 'error': 'Bad data passed in. Try again.'})