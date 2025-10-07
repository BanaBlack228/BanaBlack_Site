from django.urls import path
from . import views

app_name = 'banablack'
urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('album/', views.album, name='album'),
    path('', views.main_page, name='main_page'),
]