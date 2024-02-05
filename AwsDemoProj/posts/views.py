from django.shortcuts import render
from .models import Post

# Create your views here.
 #for list
def posts_list(request):
    posts_list=Post.objects.all()
    print("helloooo")
    print(posts_list)
    return render(request, template_name='posts.html',context={'posts_list':posts_list})
