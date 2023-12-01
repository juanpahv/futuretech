from math import log
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

def signUp(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        group = Group.objects.get(name='Users')
        group.user_set.add(user)
        user.save()
        login(request, user)
        return redirect('home')
      except IntegrityError:
        return render(request, 'login.html', {'errorSignup': 'Username already taken. Please choose another username'})

def signUpAsSeller(request):
  if request.method == 'GET':
    return render(request, 'loginSeller.html')
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        group = Group.objects.get(name='Sellers')
        group.user_set.add(user)
        user.save()
        login(request, user)
        return redirect('home')
      except IntegrityError:
        return (render(request, 'loginSeller.html', {'error': 'Username already taken. Please choose another username'}))
      
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
  return render(request, 'userProfile.html')

@login_required
def sellerProfile(request):
  return render(request, 'sellerProfile.html')



