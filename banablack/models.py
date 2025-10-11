from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст Объявления")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания",editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="posts")
    image = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name="Изображение")
    slug = models.SlugField(max_length=200,unique=True,editable=False, null=True)

# Create your models here.
