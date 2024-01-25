from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts.models import Seller
from django.db import IntegrityError

def signUp(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        required_fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        for field in required_fields:
            if not request.POST.get(field):
                return render(request, 'login.html', {'errorRegister': 'Please fill all the required fields'})
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.email = request.POST['email']
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'login.html', {'errorSignup': 'Username already taken. Please choose another username'})
        else:
            return render(request, 'login.html', {'errorRegister': 'Passwords do not match'})

def signUpAsSeller(request):
    if request.method == 'GET':
        return render(request, 'loginSeller.html')
    elif request.method == 'POST':
        required_fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'public_name']
        for field in required_fields:
            if not request.POST.get(field):
                return render(request, 'loginSeller.html', {'errorRegister': 'Please fill all the required fields'})
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.email = request.POST['email']
                user.save()

                seller = Seller(userId=user, publicName=request.POST['public_name'])
                seller.save()

                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'loginSeller.html', {'error': 'Username already taken. Please choose another username'})
        else:
            return render(request, 'loginSeller.html', {'error': 'Passwords do not match'})
      
def signIn(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
      return render(request, 'login.html', {'errorLogin': 'Username or password is incorrect.'})
    login(request, user)
    return redirect('home')

@login_required
def signOut(request):
  logout(request)
  return redirect('home')

@login_required
def userProfile(request):
  user = request.user
  is_seller = Seller.objects.filter(userId=user).exists()
  if is_seller:
    return render(request, 'sellerProfile.html', {'user': user, 'seller': is_seller})
  else:
    user = User.objects.get(id=request.user.id)
    return render(request, 'userProfile.html', {'user': user})


@login_required
def sellerProfile(request):
  user = request.user
  seller = get_object_or_404(Seller, userId=user)
  return render(request, 'sellerProfile.html', {'user': user, 'seller':seller})

@login_required
def sellerCentral(request):
  return render(request, 'sellerCentral.html')

@login_required
def sellerOrders(request):
  return render(request, 'sellerOrders.html')