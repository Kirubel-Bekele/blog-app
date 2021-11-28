from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})
def post(request, kt):
    posts = Post.objects.get(id=kt)
    return render(request,'posts.html',{'posts':posts})
