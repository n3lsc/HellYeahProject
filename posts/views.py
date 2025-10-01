from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")