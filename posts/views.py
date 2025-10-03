from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def home_view(request):
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")
def about_view(request):
    return HttpResponse("<h1>Hell yeah 100'%' about</h1>")
def post_list_view(request):
    posts = Post.objects.all()
    html = "<h1>Список постов:</h1><ul>"
    for post in posts:
        html += f"<li><strong>{post.title}</strong>:{post.content[:50]} <i>{post.author}</i>...</li>"
    html += "</ul>"
    return HttpResponse(html)