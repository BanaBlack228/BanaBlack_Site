from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def main_page(request):
    context = {"title": "Главная страница"}
    return render(request, 'main_page.html', context=context)

def album(request):
    context = {"title": "Альбомы"}
    return render(request, 'album.html', context=context)

def contact(request):
    context = {"title": "Контакт"}
    return render(request, 'contact.html', context=context)

def about_banablack(request):
    context = {"title": "О BanaBlack"}
    return render(request, 'about.html', context=context)

def single(request):
    context = {"title": "О BanaBlack"}
    return render(request, 'single.html', context=context)


# Create your views here.
