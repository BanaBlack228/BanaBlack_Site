from django.shortcuts import render

def blog(request):
    context = {"title": "Альбомы"}
    return render(request, 'blog.html', context=context)

# Create your views here.
