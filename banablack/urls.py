from django.urls import path
from banablack.views import main_page

app_name = 'banablack'
urlpatterns = [
    path('', main_page, name='main_page'),
]