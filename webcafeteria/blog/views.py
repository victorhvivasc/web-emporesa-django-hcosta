from django.shortcuts import render, get_object_or_404
from .models import post, Category

# Create your views here.
def Blog(request):
    posts = post.objects.all()
    return render(request, "blog/blog.html", {'post':posts})

def category(request, category_id):
    categoria = get_object_or_404(Category, id=category_id)
    return render(request, "blog/blog2.html", {"categorias": categoria})