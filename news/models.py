from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="название новости")
    content = models.TextField(verbose_name="текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

class Comment(models.Model):
    content = models.TextField(verbose_name="текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', verbose_name="новость")    