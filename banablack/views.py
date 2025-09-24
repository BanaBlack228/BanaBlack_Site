from django.shortcuts import render

def main_page(request):
    context = {"title": "Главная страница"}
    return render(request, 'main_page.html', context=context)

def album(request):
    context = {"title": "Альбомы"}
    return render(request, 'album.html', context=context)
# Create your views here.
