from django.shortcuts import render
from numpy import generic

class IndexLogIn(generic.FormView):
  template_name = 'userauth/index.html'
  