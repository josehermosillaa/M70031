from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blogsite/index.html', context)

def add(request):
    return render(request, 'blogsite/agregar.html')

def addregister(request):
    titulo = request.POST['title']
    contenido = request.POST['content']
    autor = request.POST['author']
    post = Post(title=titulo, content=contenido, author=autor)
    post.save()
    return HttpResponseRedirect(reverse('index'))
