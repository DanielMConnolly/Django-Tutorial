
from django.shortcuts import render

from .models import Post



def postList(request):
    postList = Post.objects.all()
    context= {"listOfPosts": postList}
    return render(request, "blog/blogList.html", context)

def blogPost(request, postId):
    blog = Post.objects.get(pk=postId)
    context = {"blog": blog}
    return render(request, "blog/blogPost.html", context)

