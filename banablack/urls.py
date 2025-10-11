from django.urls import path
from . import views

app_name = 'banablack'
urlpatterns = [
    path('single/', views.single, name='single'),
    path('banablack/', views.about_banablack, name='banablack'),
    path('contact/', views.contact, name='contact'),
    path('album/', views.album, name='album'),
    path('', views.main_page, name='main-page'),
]