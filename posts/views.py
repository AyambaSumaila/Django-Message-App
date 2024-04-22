from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class HomePageView(ListView):

    model=Post 

    template_name='home.html'
    context_object_name='all_posts_list'

# Create your views here.
"""
class AboutPageView(ListView):

    model=Post 

    template_name='about.html'
    context_object_name='all_posts_list'
"""