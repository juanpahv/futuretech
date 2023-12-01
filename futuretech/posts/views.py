from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def productPage(request):
    return render(request, 'productPage.html')

def modifyPost(request):
    return render(request, 'modifyPost.html')