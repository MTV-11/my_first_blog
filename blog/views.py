from time import time
from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    #Use QuerySet and save filter in a variable
    #This is show in the portal with a specific <div> in html text 'post_list.html' 
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})